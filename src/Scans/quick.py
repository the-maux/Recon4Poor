import os
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


def parse_result_txt():
    """ open result.txt and return the content as list(String) """
    return list()


def exec_tools(cmd, usefFile=False):
    print(f'(DEBUG) $> {cmd}')
    stdout, stderr, returncode = shell(cmd)
    if usefFile:
        urls = parse_result_txt()
        print('(DEBUG) rm -vf ./results')
        shell('rm -f ./results')
    else:
        urls = stdout.split('\n')
    urls = extract_subdomains(urls)
    return urls


def use_python_tools(target):  # arrete de dumper dans des fichiers, cest plus long que inmemory
    """
        Seach for a single domain all domain possible
        TODO: multiThread ?
    """
    cmd = f'echo {target} | python3 subcat/subcat.py -silent'
    listDomains = exec_tools(cmd=cmd, usefFile=False)

    # subdomains = sublist3r.main(domain=target, savefile='yahoo_subdomains.txt', ports=None, silent=False, verbose=False,
    #                             enable_bruteforce=False, engines=None, threads=8)
    # domains_found_Sublist3r = use_python_tool(path='Sublist3r/', tool_name='sublist3r.py',
    #                                           argv=f'-d {target} -o ./results.txt')  # &> nooutput
    # print(f"(INFO) sublist3r found: {len(domains_found_Sublist3r)} domain(s) in scope")

    # domains_found_assetfinder = use_assetfinder(target)
    # print(f"(INFO) assetfinder found: {len(domains_found_assetfinder)} url(s) in scope")
    # #TODO: aucune variable n'est retourné jte signale
    #
    # cmd = ' -l target.txt -o results.txt -san all '
    # domains_found_SubDomainizer = use_python_tool(path='SubDomainizer/', tool_name='SubDomainizer.py',
    #                                               argv=cmd) # &> nooutput
    # # TODO: SubDomainizer a etre mieux configurer, rester dans le scope du search subdomain, rien de plus
    # print(f'(INFO) SubDomainizer found: {len(domains_found_SubDomainizer)} domain(s) in scope')  # -o SubDomainizer.txt

    # TODO: subfinder cest du go boufon
    # domains_found_subfinder = use_python_tool(tool_name='subfinder', argv=f'-d {target} -silent', dumpInCmd=False)  # > subfinder.txt
    # print(f"(INFO) subfinder found: {domains_found_subfinder} domain(s) in scope")
    return listDomains


def use_go_tools(target):  # TODO: benchmark if filter_all(exec_go_tools()) is better all in one filter_all
    wayback_urls = exec_tools(cmd=f'echo "{target}" | waybackurls', usefFile=False)
    print(f'(DEBUG) Waybackurls found {len(wayback_urls)} endpoints')
    print('---------------------------------------------------------------------------------------')
    gau_urls = exec_tools(cmd=f'echo "{target}" | gau --threads 5', usefFile=False)
    print(f'(DEBUG) gau found {len(gau_urls)} endpoints')
    print('---------------------------------------------------------------------------------------')
    subfinder = exec_tools(cmd=f'echo {target} | subfinder -silent', usefFile=False)
    print(f'(DEBUG) subfinder found {len(subfinder)} endpoints')
    print('---------------------------------------------------------------------------------------')
    endpoints = extract_subdomains(wayback_urls + gau_urls + subfinder)
    return endpoints


def quick_scan(target):
#    results = use_go_tools(target)
    results = use_python_tools(target)
    return results


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
