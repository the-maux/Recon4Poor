import os, time
from threading import Thread
from src.Utils.sanitize import extract_subdomains_and_dump, check_alives_domains, strip_domains
from src.Utils.shell import shell, VERBOSE


def exec_tools(cmd, usefFile=False, tool_name=None):
    """ Execute a command and return a list of domains """
    stdout = shell(cmd, verbose=False, outputOnly=True)
    if usefFile:  # sometimes results is in stdout and sometimes dumped in a file named results.txt','
        stdout = shell('cat results.txt', verbose=False, outputOnly=True)
        shell('rm -f results.txt', verbose=False)
    subdomains = strip_domains(stdout.split('\n'), tool_name=tool_name)
    # if tool_name is not None:
    #     with open(tool_name + '.txt', 'w') as f:
    #         for item in subdomains:
    #             f.write(f"{item}\n")
    return subdomains


def use_python_tools(target, medium=False):
    """ Use python script subcat & sublist3r & SubDomainzer """
    start_python = time.time()
    subcat_res = exec_tools(cmd=f'echo {target} | python subcat/subcat.py -silent', tool_name="subcat")
    sublist3r_res = exec_tools(cmd=f'python Sublist3r/sublist3r.py -d {target} -n -o results.txt', usefFile=True)
    cmd = f'python SubDomainizer/SubDomainizer.py -u {target} -san all -o results.txt'
    subDomainizer_res = exec_tools(cmd=cmd, usefFile=True, tool_name='SubDomainizer')
    python_results = extract_subdomains_and_dump(subcat_res + sublist3r_res + subDomainizer_res)
    if not medium:
        print(f"(Py-Thread) subcat found: {len(subcat_res)} endpoints")  # le tupe de var doit etre sanityze
        print(f"(Py-Thread) sublist3r found: {len(sublist3r_res)} endpoints")
        print(f'(Py-Thread) subDomainizer found: {len(subDomainizer_res)} endpoints')
        print(f'(Py-Thread) PYTHON SCRIPTS FOUND {len(python_results)} DOMAIN in {time.time() - start_python} seconds')
    return python_results


def use_go_tools(target, medium=False):
    """ Go binary assetfinder & waybackurls & gau & subfinder """
    start = time.time()
    wayback_urls = exec_tools(cmd=f'echo {target} | waybackurls', tool_name="waybackurls")
    assetfinder_urls = exec_tools(cmd=f'echo {target} | assetfinder -subs-only ', tool_name='3')
    gau_urls = exec_tools(cmd=f'echo {target} | gau --threads 5', tool_name='2')
    subfinder = exec_tools(cmd=f'echo {target} | subfinder -silent', tool_name='1')
    go_result = extract_subdomains_and_dump(wayback_urls + gau_urls + subfinder + assetfinder_urls)
    if not medium:
        print(f'(Go-Thread) assetfinder found {len(assetfinder_urls)} domains')
        print(f'(Go-Thread) waybackurls found {len(wayback_urls)} endpoints')
        print(f'(Go-Thread) gau found {len(gau_urls)} endpoints')
        print(f'(Go-Thread) subfinder found {len(subfinder)} endpoints')
        print(f'(Go-Thread) GO tools found {len(go_result)} subdomains in {time.time() - start} seconds !')
    return go_result


def quick_scan(target, medium=False, idxThreadsMedium=0):
    """ Start 2 threads with tools, dump result in file, filter the results and return them as list of domains """
    start, pThreads  = time.time(), list()
    pThreads.append(Thread(target=use_go_tools, args=(target, medium)))
    pThreads.append(Thread(target=use_python_tools, args=(target, medium)))
    [process.start() for process in pThreads]
    [process.join() for process in pThreads]

    # domains = check_alives_domains(nameFile="tmp-search.txt")
    # extract_subdomains_and_dump(domains, medium=medium)
    domains = shell(f'cat tmp-search.txt', verbose=False, outputOnly=True).split('\n')
    print(f'(DEBUG) {target} found {len(domains)} SUBDOMAIN in {int(time.time() - start)} seconds !')
    return domains
