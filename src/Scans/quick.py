import os, time
from threading import Thread
from src.Utils.Sanitize import extract_subdomains
from src.Utils.Shell import shell, VERBOSE


def exec_tools(cmd, usefFile=True):
    print('---------------------------------')
    print(f'(DEBUG) $> {cmd}')
    stdout, stderr, returncode = shell(cmd)
    if usefFile:
        stdout, stderr, returncode = shell('cat results.txt', verbose=False)
        shell('rm -f ./results', verbose=False)
    return extract_subdomains(stdout.split('\n'))


def use_python_tools(target):
    """ Use python script subcat & sublist3r & SubDomainzer """
    cmd = f'echo {target} | python3 subcat/subcat.py -silent'
    subcat_res = exec_tools(cmd=cmd, usefFile=False)
    print(f"(DEBUG) Subcat found: {len(subcat_res)} domain(s) in scope")

    cmd = f'python3 Sublist3r/sublist3r.py -d {target} -n -o ./results.txt'
    sublist3r_res = exec_tools(cmd=cmd, usefFile=True)
    print(f"(DEBUG) Sublist3r found: {len(sublist3r_res)} domain(s) in scope")

    cmd = f'python3 SubDomainizer/SubDomainizer.py -u {target} -san all -o result.txt'
    subDomainizer_res = exec_tools(cmd=cmd, usefFile=True)
    print(f'(DEBUG) SubDomainizer found: {len(subDomainizer_res)} domain(s) in scope')

    return extract_subdomains(subcat_res + sublist3r_res + subDomainizer_res)


def use_go_tools(target):
    """ User Go binary waybackurls & gau & subfinder """
    wayback_urls = exec_tools(cmd=f'echo "{target}" | waybackurls', usefFile=False)
    print(f'(DEBUG) Waybackurls found {len(wayback_urls)} endpoints')

    gau_urls = exec_tools(cmd=f'echo "{target}" | gau ', usefFile=False)  # --threads 5 ?
    print(f'(DEBUG) gau found {len(gau_urls)} endpoints')

    subfinder = exec_tools(cmd=f'echo {target} | subfinder -silent', usefFile=False)
    print(f'(DEBUG) subfinder found {len(subfinder)} endpoints')

    subdomains = extract_subdomains(wayback_urls + gau_urls + subfinder)
    return subdomains


def quick_scan(target):
    start = time.time()
    go_results = use_go_tools(target)
    end_go = time.time()
    print(f'(DEBUG) GO TOOLS FOUND {len(go_results)} SUBDOMAIN in {end_go - start} seconds !\n')

    start_python = time.time()
    python_results = use_python_tools(target)
    end_python = time.time()
    print(f'(DEBUG) PYTHON TOOLS FOUND {len(go_results)} SUBDOMAIN in {end_python - start_python} seconds ! \n')

    final_res = extract_subdomains(go_results + python_results)
    print(f'(DEBUG) ALL TOOLS FOUND {len(final_res)} SUBDOMAIN in {end_python - start_python} seconds ! ')
    return final_res


# def quick_scan_parrall(target): # ca dump dans des fichiers, mais il faut le recup in memory mais cest en thread :/
#     listOfToolsToExec = list()
#     p1 = Thread(target=use_python_tool, args=('./tools/SubDomainizer/', 'SubDomainizer.py', ' -l target.txt -o SubDomainizer.txt -san all  &> nooutput'))
#     p2 = Thread(target=use_python_tool, args=('subfinder', f'-d {target} -silent'))
#     p3 = Thread(target=use_python_tool, args=('./tools/Sublist3r/', 'sublist3r.py', f'-d {target} -o sublist3r.txt &> nooutput'))
#     p4 = Thread(target=use_assetfinder, args=(target))
#     listOfToolsToExec.append(p1)
#     listOfToolsToExec.append(p2)
#     listOfToolsToExec.append(p3)
#     listOfToolsToExec.append(p4)
#     [process.start() for process in listOfToolsToExec]
#     [process.join() for process in listOfToolsToExec]


# domains_found_assetfinder = use_assetfinder(target)
# print(f"(INFO) assetfinder found: {len(domains_found_assetfinder)} url(s) in scope")
# shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt