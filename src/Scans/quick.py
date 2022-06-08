import os, time
from threading import Thread
from src.Utils.Sanitize import extract_subdomains_and_dump
from src.Utils.Shell import shell, VERBOSE


def exec_tools(cmd, usefFile=True):
    stdout, stderr, returncode = shell(cmd, verbose=False)
    if usefFile:
        stdout, stderr, returncode = shell('cat results.txt', verbose=False)
        shell('rm -f results.txt', verbose=False)
    return stdout.split('\n')


def use_python_tools(target):
    """ Use python script subcat & sublist3r & SubDomainzer """
    start_python = time.time()
    print('(Python-Thread) Starting Python scripts with subcat :)')

    subcat_res = exec_tools(cmd=f'echo {target} | python3 subcat/subcat.py -silent', usefFile=False)
    print(f"(Python-Thread) Subcat found: {len(subcat_res)} endpoints in scope")

    sublist3r_res = exec_tools(cmd=f'python3 Sublist3r/sublist3r.py -d {target} -n -o results.txt', usefFile=True)
    print(f"(Python-Thread) Sublist3r found: {len(sublist3r_res)} endpoints in scope")

    cmd = f'python3 SubDomainizer/SubDomainizer.py -u {target} -san all -o results.txt'
    subDomainizer_res = exec_tools(cmd=cmd, usefFile=True)
    print(f'(Python-Thread) SubDomainizer found: {len(subDomainizer_res)} endpoints in scope')

    python_results = extract_subdomains_and_dump(subcat_res + sublist3r_res + subDomainizer_res)
    print(f'(Python-Thread) PYTHON SCRIPTS FOUND {len(python_results)} SUBDOMAIN in {time.time() - start_python} seconds ! \n')
    return python_results


def use_go_tools(target):
    """ User Go binary waybackurls & gau & subfinder """
    start = time.time()
    print('(Go-Thread) Starting Go Tools with subcat :)')

    wayback_urls = exec_tools(cmd=f'echo "{target}" | waybackurls', usefFile=False)
    print(f'(Go-Thread) Waybackurls found {len(wayback_urls)} endpoints')

    gau_urls = exec_tools(cmd=f'echo "{target}" | gau ', usefFile=False)  # --threads 5 ?
    print(f'(Go-Thread) gau found {len(gau_urls)} endpoints')

    subfinder = exec_tools(cmd=f'echo {target} | subfinder -silent', usefFile=False)
    print(f'(Go-Thread) subfinder found {len(subfinder)} endpoints')

    subdomains = extract_subdomains_and_dump(wayback_urls + gau_urls + subfinder)
    print(f'(Go-Thread) GO TOOLS DUMPED {len(subdomains)} SUBDOMAIN in {time.time() - start} seconds !\n')
    return subdomains


def quick_scan(target):
    start = time.time()
    pThreads = list()
    pThreads.append(Thread(target=use_go_tools, args=(target,)))
    pThreads.append(Thread(target=use_python_tools, args=(target,)))
    [process.start() for process in pThreads]
    [process.join() for process in pThreads]
    stdout, stderr, returncode = shell('cat tmp-search.txt', verbose=False)
    resultats = extract_subdomains_and_dump(stdout.split('\n'), dump=False)
    print(f'(DEBUG) PARALL // TOOLS FOUND {len(resultats)} SUBDOMAIN in {time.time() - start} seconds !\n')
    return resultats


# domains_found_assetfinder = use_assetfinder(target)
# print(f"(INFO) assetfinder found: {len(domains_found_assetfinder)} urls in scope")
# shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt