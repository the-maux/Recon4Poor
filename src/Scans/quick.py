import os
from threading import Thread
from src.Utils.Shell import shell, VERBOSE


def use_assetfinder(target):
    """
        les resultats sont dnas le fichier: assetfinder_urls.txt
        #TOKNOW: assetfinder is not working good with "https://"
    """
    listResult = list()
    stdout, stderr, returncode = shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt
    return listResult  # TODO: mettre assetfinder_urls.txt in listResult


def use_python_tool(tool_name='echo ', argv='', path='', dumpInCmd=False):
    """
        Use a specific python tool to do a search subdomain, dump founds in results.txt file
        TOKNOW: convert results.txt as python list
        TOKNOW: remove the results.txt in current workspace
        return: list of strings who was inside the result.txt
    """
    listResult = list()
    print(f'\n\n-----------------------------------------------------------------')
    print(f'(INFO) [+] Using tool with {tool_name}')
    cmd = f'python {path}{tool_name} {argv}'
    stdout, stderr, returncode = shell(cmd if dumpInCmd is False else cmd + '> ./results.txt')
    if VERBOSE:
        print(f'(DEBUG) cmd > {cmd if dumpInCmd is False else cmd + "> ./results.txt"}')
        print(f'(DEBUG) stdout >\n {stdout}')
        print(f'(DEBUG) stderr >\n {stderr}')
        print(f'(DEBUG) return status code  > {returncode}')
    print('---------------------------------------------------------------------------------------')
    print('(DEBUG) cat ./results.txt')
    os.system('cat ./results.txt')
    print('---------------------------------------------------------------------------------------')
    print('(DEBUG) rm -vf ./results.txt')
    shell('rm -vf ./results.txt')
    return listResult


def search_4_domains(target):  # arrete de dumper dans des fichiers, cest plus long que inmemory
    """
        Seach for a single domain all domain possible
        TODO: multiThread ?
    """
    # subdomains = sublist3r.main(domain=target, savefile='yahoo_subdomains.txt', ports=None, silent=False, verbose=False,
    #                             enable_bruteforce=False, engines=None, threads=8)
    domains_found_Sublist3r = use_python_tool(path='Sublist3r/', tool_name='sublist3r.py',
                                              argv=f'-d {target} -o ./results.txt')  # &> nooutput
    print(f"(INFO) sublist3r found: {len(domains_found_Sublist3r)} domain(s) in scope")

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


def quick_scan(target):
    results = list()
    search_4_domains(target)

    return results


def quick_scan_parrall(target): # ca dump dans des fichiers, mais il faut le recup in memory mais cest en thread :/
    listOfToolsToExec = list()
    p1 = Thread(target=use_python_tool, args=('./tools/SubDomainizer/', 'SubDomainizer.py', ' -l target.txt -o SubDomainizer.txt -san all  &> nooutput'))
    p2 = Thread(target=use_python_tool, args=('subfinder', f'-d {target} -silent'))
    p3 = Thread(target=use_python_tool, args=('./tools/Sublist3r/', 'sublist3r.py', f'-d {target} -o sublist3r.txt &> nooutput'))
    p4 = Thread(target=use_assetfinder, args=(target))
    listOfToolsToExec.append(p1)
    listOfToolsToExec.append(p2)
    listOfToolsToExec.append(p3)
    listOfToolsToExec.append(p4)
    [process.start() for process in listOfToolsToExec]
    [process.join() for process in listOfToolsToExec]
