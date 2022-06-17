import os, time
from threading import Thread
from src.Utils.Sanitize import extract_subdomains_and_dump, check_alives_domains
from src.Utils.Shell import shell, VERBOSE


def exec_tools(cmd, usefFile=False):
    stdout, stderr, returncode = shell(cmd, verbose=False)
    if usefFile:
        stdout, stderr, returncode = shell('cat results.txt', verbose=False)
        shell('rm -f results.txt', verbose=False)
    return stdout.split('\n')


def use_python_tools(target):
    """ Use python script subcat & sublist3r & SubDomainzer """
    start_python = time.time()
    print('(Py-Thread) Starting Python scripts with subcat')

    subcat_res = exec_tools(cmd=f'echo "{target}" | python3 subcat/subcat.py -silent')
    print(f"(Py-Thread) Subcat found: {len(subcat_res)} endpoints")

    sublist3r_res = exec_tools(cmd=f'python3 Sublist3r/sublist3r.py -d "{target}" -n -o results.txt', usefFile=True)
    print(f"(Py-Thread) Sublist3r found: {len(sublist3r_res)} endpoints")

    cmd = f'python3 SubDomainizer/SubDomainizer.py -u "{target}" -san all -o results.txt'
    subDomainizer_res = exec_tools(cmd=cmd, usefFile=True)
    print(f'(Py-Thread) SubDomainizer found: {len(subDomainizer_res)} endpoints')

    python_results = extract_subdomains_and_dump(subcat_res + sublist3r_res + subDomainizer_res)
    print(f'(Py-Thread) PYTHON SCRIPTS FOUND {len(python_results)} DOMAIN in {time.time() - start_python} seconds')

    return python_results


def use_go_tools(target):
    """ User Go binary waybackurls & gau & subfinder """
    start = time.time()
    print('(Go-Thread) Starting Go Tools with waybackurls')

    assetfinder_urls = exec_tools(cmd=f'echo "{target}" | assetfinder -subs-only ')
    print(f'(Go-Thread) Assetfinder found {len(assetfinder_urls)} endpoints')
    print()
    wayback_urls = exec_tools(cmd=f'echo "{target}" | waybackurls')
    if len(wayback_urls) == 1:
        print(wayback_urls)
    print(f'(Go-Thread) Waybackurls found {len(wayback_urls)} endpoints')

    gau_urls = exec_tools(cmd=f'echo "{target}" | gau ')  # --threads 5 ?
    print(f'(Go-Thread) gau found {len(gau_urls)} endpoints')

    subfinder = exec_tools(cmd=f'echo "{target}" | subfinder -silent')
    print(f'(Go-Thread) subfinder found {len(subfinder)} endpoints')

    go_result = extract_subdomains_and_dump(wayback_urls + gau_urls + subfinder)
    print(f'(Go-Thread) GO TOOLS DUMPED {len(go_result)} SUBDOMAIN in {time.time() - start} seconds !')

    return go_result


def quick_scan(target):
    start = time.time()
    pThreads = list()
    pThreads.append(Thread(target=use_go_tools, args=(target,)))
    pThreads.append(Thread(target=use_python_tools, args=(target,)))
    [process.start() for process in pThreads]
    [process.join() for process in pThreads]
    stdout, stderr, returncode = shell('cat tmp-search.txt', verbose=False)
    #TODO: quand est ce quon  check si cest alive ? afin de relancer le regularscan avec les bon subDomainizer_re
    #TODO: quand tu vas lancer des multi hreads pour du quick scan avec les sbdomain, y a un probleme avec le namefile tmp-result.txt
    domain_offline, domain_alive = check_alives_domains(stdout.split('\n'))
    resultats = extract_subdomains_and_dump(domain_alive, dump=False)
    print(f'(Main-Thread) Found {len(domain_alive)} domain alives and {len(domain_offline)} domain offline')
    print(f'(DEBUG) PARALL // TOOLS FOUND {len(resultats)} SUBDOMAIN in {time.time() - start} seconds !\n')
    return resultats


# print(f"(INFO) assetfinder found: {len(domains_found_assetfinder)} urls in scope")
# shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt