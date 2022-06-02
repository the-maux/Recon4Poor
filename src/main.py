import os
from src.Utils.Sanitize import sanitize_my_domain, sanity_check_at_startup
from src.Scans.quick import quick_scan
from src.Scans.regular import regular_scan
from src.Scans.hard import hard_scan
from src.Analyze.analyze import searching_assets, search_JS_files
from src.Analyze.report import generate_report
from src.Analyze.send_report import sendMail

def regroup_found_and_filter():
    """

    :return:
    """
    print("(DEBUg) [+] Filtering results \e[0m")
    #  number_of_file_found=$(cat all_urls.txt | wc -l)
    number_of_file_found = 42  # TODO: extract nbr of url
    print(f"(INFO) Before filter duplicate/offline/useless files, found: {number_of_file_found} files to analyse")
    # filtering dead link
    #cat all_js_files_found.txt | httpx -follow-redirects -status-code -silent | grep "[200]" | cut -d ' ' -f1 > urls_alive.txt
    # filtering duplicate & libs with no impact
    # cat all_js_files_found.txt | awk -F '?' '{ print $1 }' | grep -v "jquery" | grep $(cat target.txt | sed 's$https://$$') | sort -u > urls.txt

    #number_of_file_found=$(cat urls.txt | wc -l)
    number_of_file_found = 24 # TODO: extract nbr of url
    print(f"(INFO) Result of filters: Found $((number_of_file_found)) javascripts files to analyse")

    #cat urls.txt | grep $(cat target.txt | sed 's$https://$$') > urls_filter.txt  # Only take if target domain is present
    #number_of_file_found_post_filter=$(cat urls_filter.txt | wc -l)
    number_of_file_found_post_filter = 53
    print(f"(INFO) Result of BIG filters: Found {number_of_file_found_post_filter} javascripts files to analyse")
    return number_of_file_found


def search_domains(target_domain, depth):
    """
        return une liste de domain
        quick_scan: # result in gau_solo_urls.txt subjs_url.txt hakrawler_urls.txt gospider_url.txt
        regular_scan: # result TODO: les results ne doivent plus etre stocké dans des fichiers mais in memory
        hard_scan: # result
    """
    print(f'Searching Domains on target(s): {target} with depth {depth}')
    os.system(f'echo "{target_domain}" >> target.txt')
    if depth == "1":
        urls_list = quick_scan(target_domain)
    elif depth == "2":
        urls_list = regular_scan(target_domain)
    else:
        urls_list = hard_scan(target_domain)
    urls_list = sanitize_my_domain(urls_list)
    return urls_list


def global_controller(target, depth):
    """
        From 1 domain, search for maximum subdomain than search for JS file
    """
    domains = search_domains(target, depth) # resulst est une list de subdomain (TODO: filtered by allowed scope)
    if len(domains) < 1:
        print('(ERROR) no subdomain found for this target')
        exit(-1)
    # assets_found = search_JS_files(domains)
    # # TODO: searchin JS & Secret Here
    # report = generate_report(domains, assets_found)
    # sendMail(report)


if __name__ == "__main__":
    # TODO: install check, if not present, start it
    target, depth = sanity_check_at_startup()
    global_controller(target, depth)
