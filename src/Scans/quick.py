from src.Utils.Shell import shell


def use_python_tool(tool_name='echo ', argv='',
                    path=''):  # TODO: tu as oublié de faire la distinction entre python et pas python dans lexec
    listResult = list()
    print(f'(INFO) [+] Using tool with {tool_name}')
    stdout, stderr, returncode = shell(f'python {path}{tool_name} {argv}')
    print(f'-----------------------------------------------------------------')
    print(stdout)
    return listResult  # TODO: mettre les dump *.txt dans la var listResult


def use_assetfinder(target):
    """
        les resultats sont dnas le fichier: assetfinder_urls.txt
        #TOKNOW: assetfinder is not working good with "https://"
    """
    listResult = list()
    stdout, stderr, returncode = shell("cat target.txt | sed 's$https://$$' | assetfinder -subs-only ") # | sort -u > assetfinder_urls.txt
    return listResult  # TODO: mettre assetfinder_urls.txt in listResult


def search_4_domains(target):  # arrete de dumper dans des fichiers, cest plus long que inmemory
    """
        Seach for a single domain all domain possible
        TODO: multiThread ?
    """
    print('(DEBUG) Searching with chaos & gau & subjs & hakrawler & assetfinder & gospider')

    domains_found_SubDomainizer = use_python_tool(path='./tools/SubDomainizer/', tool_name='SubDomainizer.py',
                                                  argv=' -l target.txt -o SubDomainizer.txt -san all  &> nooutput')
    print(f'(INFO) SubDomainizer found: {len(domains_found_SubDomainizer)} domain(s) in scope')  # -o SubDomainizer.txt

    domains_found_subfinder = use_python_tool(tool_name='subfinder', argv='-d $target -silent')  # > subfinder.txt
    print(f"(INFO) subfinder found: {domains_found_subfinder} domain(s) in scope")

    domains_found_Sublist3r = use_python_tool(path='./tools/Sublist3r/', tool_name='sublist3r.py',
                                              argv='-d $target -o sublist3r.txt &> nooutput')  #  -o sublist3r.txt
    print(f"(INFO) sublist3r found: {len(domains_found_Sublist3r)} domain(s) in scope")

    domains_found_assetfinder = use_assetfinder(target)
    print(f"(INFO) assetfinder found: {len(domains_found_assetfinder)} url(s) in scope")


def quick_scan(target):
    results = list()
    search_4_domains(target)
    return results
