import os, time
from threading import Thread
from src.Utils.Sanitize import extract_subdomains_and_dump, check_alives_domains
from src.Utils.Shell import shell, VERBOSE


def exec_tools(cmd, usefFile=False):
    """ Execute a command and return a list of domains """
    result = list()
    try:
        stdout = shell(cmd, verbose=False, outputOnly=True)
        if usefFile:  # sometimes results is in stdout and sometimes dumped in a file named results.txt','
            stdout = shell('cat results.txt', verbose=False, outputOnly=True)
            shell('rm -f results.txt', verbose=False)
        result = stdout.split('\n')
    except Exception as e:
        print(e)
    return result


def use_python_tools(target):
    """ Use python script subcat & sublist3r & SubDomainzer """
    start_python = time.time()

    subcat_res = exec_tools(cmd=f'echo "{target}" | python subcat/subcat.py -silent')
    print(f"(Py-Thread) Subcat found: {len(subcat_res)} endpoints") # le tupe de var doit etre sanityze

    sublist3r_res = exec_tools(cmd=f'python Sublist3r/sublist3r.py -d "{target}" -n -o results.txt', usefFile=True)
    print(f"(Py-Thread) Sublist3r found: {len(sublist3r_res)} endpoints")

    cmd = f'python SubDomainizer/SubDomainizer.py -u "{target}" -san all -o results.txt'
    subDomainizer_res = exec_tools(cmd=cmd, usefFile=True)
    print(f'(Py-Thread) SubDomainizer found: {len(subDomainizer_res)} endpoints')

    python_results = extract_subdomains_and_dump(subcat_res + sublist3r_res + subDomainizer_res)
    print(f'(Py-Thread) PYTHON SCRIPTS FOUND {len(python_results)} DOMAIN in {time.time() - start_python} seconds')

    return python_results


def use_go_tools(target):
    """ User Go binary waybackurls & gau & subfinder """
    start = time.time()

    # assetfinder_urls = exec_tools(cmd=f'echo "{target}" | assetfinder -subs-only ')
    # print(f'(Go-Thread) Assetfinder found {len(assetfinder_urls)} endpoints')
    # print()
    wayback_urls = exec_tools(cmd=f'echo "{target}" | waybackurls')
    print(f'(Go-Thread) Waybackurls found {len(wayback_urls)} endpoints')

    gau_urls = exec_tools(cmd=f'echo "{target}" | gau ')  # --threads 5 ?
    print(f'(Go-Thread) gau found {len(gau_urls)} endpoints')

    subfinder = exec_tools(cmd=f'echo "{target}" | subfinder -silent')
    print(f'(Go-Thread) subfinder found {len(subfinder)} endpoints')

    go_result = extract_subdomains_and_dump(wayback_urls + gau_urls + subfinder)
    print(f'(Go-Thread) GO TOOLS DUMPED {len(go_result)} SUBDOMAIN in {time.time() - start} seconds !')

    return go_result


def quick_scan(target):
    """ Start 2 threads with tools, dump result in file, filter the results and return them as list of domains """
    start, pThreads  = time.time(), list()
    pThreads.append(Thread(target=use_go_tools, args=(target,)))
    pThreads.append(Thread(target=use_python_tools, args=(target,)))
    [process.start() for process in pThreads]
    [process.join() for process in pThreads]
    stdout = shell(cmd='cat tmp-search.txt', verbose=False, outputOnly=True)
    domain_offline, domain_alive = check_alives_domains(stdout.split('\n'))
    resultats = extract_subdomains_and_dump(domain_alive, dump=False)
    print(f'(Main-Thread) Found {len(domain_alive)} domain alives and {len(domain_offline)} domain offline')
    print(f'(DEBUG) Py+GO tools found {len(resultats)} SUBDOMAIN in {time.time() - start} seconds !')
    return resultats


# print(f"(INFO) assetfinder found: {len(domains_found_assetfinder)} urls in scope")
# shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt