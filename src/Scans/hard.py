from src.Utils.Shell import shell


def hitme(nameFile='all_js_files_found.txt'):
    print(f'[+] Searching JsFiles-links mixing gau & subjs & assetfinder')
    shell(f"cat {nameFile} | sed 's$https://$$' | chaos -silent | waybackurls | httpx -silent", outputOnly=True)
    shell(f'cat {nameFile} | hakrawler -js -plain -usewayback -depth 3 -scope subs | unew')
    shell(f"cat {nameFile} | sed 's$https://$$' | assetfinder -subs-only | httpx -threads 300 --follow-redirects -silent | sort -u")
    # TOKNOW: gospider is not working good without the "https://"
    shell(f'gospider -a -w -r -S {nameFile} -d 3 | grep -Eo "(http|https)://[^/\"].*\.js+" | sed "s#\] \- #\n#g"')


def regroup_found_and_filter(nameFile='all_js_files_found.txt'):
    """ nia nia nia """
    shell(f'cat {nameFile} | httpx -follow-redirects -status-code -silent | grep "[200]" | cut -d " " -f1', outputOnly=True)
    # filtering duplicate & libs with no impact
    shell(f'cat {nameFile} | ' + "awk -F '?' '{ print $1 }' " + '| grep -v "jquery" | grep $(cat target.txt | ' +
            "sed 's$https://$$') | sort -u")
    return 42


def hard_scan(target):
    print('(DEBUG) Starting brutal scan')
    results = list()
    return results
