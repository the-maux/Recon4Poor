import os
from src.Utils.Sanitize import sanity_check_at_startup, final_sanityze
from src.Scans.quick import quick_scan
from src.Scans.regular import regular_scan
from src.Scans.hard import hard_scan
from src.Analyze.analyze import searching_assets, search_JS_files
from src.Analyze.report import generate_report
from src.Analyze.send_report import sendMail


def regroup_found_and_filter():
    # cat all_js_files_found.txt | httpx -follow-redirects -status-code -silent | grep "[200]" | cut -d ' ' -f1 > urls_alive.txt
    # filtering duplicate & libs with no impact
    # cat all_js_files_found.txt | awk -F '?' '{ print $1 }' | grep -v "jquery" | grep $(cat target.txt | sed 's$https://$$') | sort -u > urls.txt
    #cat urls.txt | grep $(cat target.txt | sed 's$https://$$') > urls_filter.txt  # Only take if target domain is present
    #number_of_file_found_post_filter=$(cat urls_filter.txt | wc -l)
    return 42


def search_domains(target_domain, depth):
    """
        return une liste de domain
        quick_scan: # result in gau_solo_urls.txt subjs_url.txt hakrawler_urls.txt gospider_url.txt
        regular_scan: # result TODO: les results ne doivent plus etre stocké dans des fichiers mais in memory
        hard_scan: # result
    """
    print(f'Searching Domains on target(s): {target} with depth {depth}')
    os.system(f'echo "{target_domain}" >> target.txt')
    if depth == 1:
        urls_list = quick_scan(target_domain)
    elif depth == 2:
        urls_list = regular_scan(target_domain)
    else:
        urls_list = hard_scan(target_domain)
    return urls_list


def build_rapport(domains):
    domains_offline, domains_alive = final_sanityze(domains)
    with open('domains.txt', 'w') as f:
        for item in domains:
            f.write(f"{item}\n")
    with open('domains-alive.txt', 'w') as f:
        for item in domains_alive:
            f.write(f"{item}\n")
    with open('domains-offline.txt', 'w') as f:
        for item in domains_alive:
            f.write(f"{item}\n")


def global_controller(target, depth):
    """ From 1 domain, search for maximum subdomain than search for JS file """
    endpoints = search_domains(target, depth)  # resulst est une list de subdomain (TODO: filtered by allowed scope)
    if len(endpoints) < 1:
        print('(ERROR) no subdomain found for this target')
        exit(-1)
    else:
        print(f'(DEBUG) At the end found {len(endpoints)} endpoints')
        build_rapport(endpoints)
        exit(0)
    # assets_found = search_JS_files(domains)
    # # TODO: searchin JS & Secret Here
    # report = generate_report(domains, assets_found)
    # sendMail(report)


if __name__ == "__main__":
    target, depth = sanity_check_at_startup()
    global_controller(target, depth)
