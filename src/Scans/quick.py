import os, time
from threading import Thread
from src.Utils.Sanitize import extract_subdomains_and_dump
from src.Utils.Shell import shell, VERBOSE


def exec_tools(cmd, usefFile=True):
    print('---------------------------------')
    stdout, stderr, returncode = shell(cmd)
    if usefFile:
        stdout, stderr, returncode = shell('cat results.txt', verbose=True)
        shell('rm -f ./results', verbose=False)
    return stdout.split('\n')


def use_python_tools(target):
    """ Use python script subcat & sublist3r & SubDomainzer """
    start_python = time.time()

    cmd = f'echo {target} | python3 subcat/subcat.py -silent'
    subcat_res = exec_tools(cmd=cmd, usefFile=False)
    print(f"(DEBUG) Subcat found: {len(subcat_res)} domain(s) in scope")

    cmd = f'python3 Sublist3r/sublist3r.py -d {target} -n -o ./results.txt'
    sublist3r_res = exec_tools(cmd=cmd, usefFile=True)
    print(f"(DEBUG) Sublist3r found: {len(sublist3r_res)} domain(s) in scope")

    cmd = f'python3 SubDomainizer/SubDomainizer.py -u {target} -san all -o result.txt'
    subDomainizer_res = exec_tools(cmd=cmd, usefFile=True)
    print(f'(DEBUG) SubDomainizer found: {len(subDomainizer_res)} domain(s) in scope')

    end_python = time.time()
    python_results = extract_subdomains_and_dump(subcat_res + sublist3r_res + subDomainizer_res)
    print(f'(DEBUG) PYTHON TOOLS FOUND {len(python_results)} SUBDOMAIN in {end_python - start_python} seconds ! \n')
    return python_results


def use_go_tools(target):
    """ User Go binary waybackurls & gau & subfinder """
    start = time.time()
    wayback_urls = exec_tools(cmd=f'echo "{target}" | waybackurls', usefFile=False)
    print(f'(DEBUG) Waybackurls found {len(wayback_urls)} endpoints')

    gau_urls = exec_tools(cmd=f'echo "{target}" | gau ', usefFile=False)  # --threads 5 ?
    print(f'(DEBUG) gau found {len(gau_urls)} endpoints')

    subfinder = exec_tools(cmd=f'echo {target} | subfinder -silent', usefFile=False)
    print(f'(DEBUG) subfinder found {len(subfinder)} endpoints')

    subdomains = extract_subdomains_and_dump(wayback_urls + gau_urls + subfinder)
    end_go = time.time()
    print(f'(DEBUG) GO TOOLS FOUND {len(subdomains)} SUBDOMAIN in {end_go - start} seconds !\n')
    return subdomains


def quick_scan(target):
    # start = time.time()
    # go_results = use_go_tools(target)
    # python_results = use_python_tools(target)
    # final_res = extract_subdomains(go_results + python_results)
    # end = time.time()
    # print(f'(DEBUG) ALL TOOLS FOUND {len(final_res)} SUBDOMAIN in {end - start} seconds ! ')
    # return final_res
    start = time.time()
    pThreads = list()
    pThreads.append(Thread(target=use_go_tools, args=(target,)))
    pThreads.append(Thread(target=use_python_tools, args=(target,)))
    [process.start() for process in pThreads]
    [process.join() for process in pThreads]
    stdout, stderr, returncode = shell('rm -f tmp-search.txt', verbose=False)
    resultats = stdout.split('\n')

    print(f'(DEBUG) PARALL TOOLS FOUND {len(resultats)} SUBDOMAIN in {time.time() - start} seconds !\n')
    return resultats


# domains_found_assetfinder = use_assetfinder(target)
# print(f"(INFO) assetfinder found: {len(domains_found_assetfinder)} url(s) in scope")
# shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt