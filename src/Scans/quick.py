import os, time
from threading import Thread
from pip._internal.utils import urls
from src.Analyze.filter_endpoint import extract_subdomains
from src.Utils.Shell import shell, VERBOSE


# def use_assetfinder(target):
#     """
#         les resultats sont dnas le fichier: assetfinder_urls.txt
#         #TOKNOW: assetfinder is not working good with "https://"
#     """
#     listResult = list()
#     stdout, stderr, returncode = shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt
#     return listResult  # TODO: mettre assetfinder_urls.txt in listResult


def use_python_tool(cmd='echo Hi', dumpInCmd=False):
    """
        Use a specific python tool to do a search subdomain, dump founds in results.txt file
        TOKNOW: remove the results.txt in current workspace
        return: list of strings who was inside the result.txt
    """
    listResult = list()
    print(f'\n\n-----------------------------------------------------------------')
    stdout, stderr, returncode = shell(cmd if dumpInCmd is False else cmd + '> ./results.txt')
    if VERBOSE:
        print(f'(DEBUG) $> {cmd if dumpInCmd is False else f"{cmd}> ./results.txt"}')
        print(f'(DEBUG) stdout >\n {stdout}')
        print(f'(DEBUG) stderr >\n {stderr}')
        print(f'(DEBUG) return status code  > {returncode}')
    print('---------------------------------------------------------------------------------------')
    shell('rm -f ./results.txt')
    return listResult


def exec_tools(cmd, usefFile=True):
    print('---------------------------------')
    print(f'(DEBUG) $> {cmd}')
    stdout, stderr, returncode = shell(cmd)
    if usefFile:
        stdout, stderr, returncode = shell('cat results.txt')
        shell('rm -f ./results')
    return extract_subdomains(stdout.split('\n'))


def use_python_tools(target):  # arrete de dumper dans des fichiers, cest plus long que inmemory
    """
        Seach from a single domain all subdomain possible
        TODO: multiThread ?
    """
    cmd = f'echo {target} | python3 subcat/subcat.py -silent'
    subcat_res = exec_tools(cmd=cmd, usefFile=False)
    print(f"(DEBUG) Subcat found: {len(subcat_res)} domain(s) in scope")

    cmd = f'python3 Sublist3r/sublist3r.py -d {target} -n -o ./results.txt'
    sublist3r_res = exec_tools(cmd=cmd, usefFile=True)
    print(f"(DEBUG) Sublist3r found: {len(sublist3r_res)} domain(s) in scope")

    cmd = f'python3 SubDomainizer/SubDomainizer.py -u {target} -san all -o result.txt'  # TODO: SubDomainizer need real conf
    subDomainizer_res = exec_tools(cmd=cmd, usefFile=True)
    print(f'(DEBUG) SubDomainizer found: {len(subDomainizer_res)} domain(s) in scope')  # -o SubDomainizer.txt

    return extract_subdomains(subcat_res + sublist3r_res + subDomainizer_res)


def use_go_tools(target):  # TODO: benchmark if filter_all(exec_go_tools()) is better all in one filter_all
    wayback_urls = exec_tools(cmd=f'echo "{target}" | waybackurls', usefFile=False)
    print(f'(DEBUG) Waybackurls found {len(wayback_urls)} endpoints')
    gau_urls = exec_tools(cmd=f'echo "{target}" | gau --threads 5', usefFile=False)
    print(f'(DEBUG) gau found {len(gau_urls)} endpoints')
    subfinder = exec_tools(cmd=f'echo {target} | subfinder -silent', usefFile=False)
    print(f'(DEBUG) subfinder found {len(subfinder)} endpoints')
    subdomains = extract_subdomains(wayback_urls + gau_urls + subfinder)
    return subdomains


def quick_scan(target):
    start = time.time()
    go_results = use_go_tools(target)
    end_go = time.time()
    print(f'(DEBUG) GO TOOLS FOUND {len(go_results)} SUBDOMAIN in {end_go - start} seconds ! ')

    start_python = time.time()
    python_results = use_python_tools(target)
    end_python = time.time()
    print(f'(DEBUG) PYTHON TOOLS FOUND {len(go_results)} SUBDOMAIN in {end_python - start_python} seconds ! ')

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
