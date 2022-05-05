from src.Utils.Shell import shell


def use_tool(tool_name='echo ', argv='', path=''): # TODO: tu as oublié de faire la distinction entre python et pas python dans lexec
    print('echo -e "\n\e[36m[+] Searching with chaos & gau & subjs & hakrawler & assetfinder & gospider \e[0m"')
    stdout, stderr, returncode = shell(f'python {path}{tool_name} {argv}')
    print(f'(DEBUG) Found {len(stdout)}')


def use_assetfinder(target):
    """
      #TOKNOW: assetfinder is not working good with "https://"
      cat target.txt | sed 's$https://$$' | assetfinder -subs-only | sort -u > assetfinder_urls.txt
      echo -n `date +"[%H:%M:%S]"` && echo -e "(INFO) assetfinder individually found: $(cat assetfinder_urls.txt | wc -l) url(s) in scope"
      cat assetfinder_urls.txt >> SubDomainizer.txt
    """
    pass


def filtering_allresult():
    """
        cat SubDomainizer.txt | sed 's$www.$$' | sort -u > urls_no_http.txt
        echo -n `date +"[%H:%M:%S]"` && echo -e "(INFO) After filtering duplicate, $(cat urls_no_http.txt | wc -l) domain(s) in scope"
        cat all_url.txt | sort -u > all_urls.txt
    """
    pass


def use_recontools_individualy(target):  # arrete de dumper dans des fichiers, cest plus long que inmemory
    print('(DEBUG) Searching with chaos & gau & subjs & hakrawler & assetfinder & gospider')

    use_tool(path='./tools/SubDomainizer/', tool_name='SubDomainizer.py', argv=' -l target.txt -o SubDomainizer.txt -san all  &> nooutput')
    print('"(INFO) SubDomainizer found: $(cat SubDomainizer.txt | wc -l) domain(s) in scope"')

    use_tool(tool_name='subfinder', argv='-d $target -silent > subfinder.txt')
    print("(INFO) subfinder found: $(cat subfinder.txt | wc -l) domain(s) in scope")

    use_tool(path='./tools/Sublist3r/', tool_name='sublist3r.py', argv='-d $target -o sublist3r.txt &> nooutput')
    print("(INFO) sublist3r found: $(cat sublist3r.txt | wc -l) domain(s) in scope")
    #      cat sublist3r.txt >> SubDomainizer.txt

    use_assetfinder(target)


def quick_scan(target):
    results = list()
    return results
