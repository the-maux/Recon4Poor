import os
from src.Utils.Sanitize import sanity_check_at_startup
from src.Scans.quick import quick_scan
from src.Scans.regular import regular_scan
from src.Scans.hard import hard_scan
from src.Analyze.report import build_rapport
from src.Analyze.analyze import searching_assets, search_JS_files
from src.Analyze.send_report import sendMail


def search_domains(target_domain, depth):
    """
        return une liste de domain
        quick_scan: # result in gau_solo_urls.txt subjs_url.txt hakrawler_urls.txt gospider_url.txt
        regular_scan: # result
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


def global_controller(target, depth):
    """ From 1 domain, search for maximum subdomain than search for JS file """
    endpoints = search_domains(target, depth)  # TODO: filtered by allowed scope
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
