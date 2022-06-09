import os
from src.Utils.Sanitize import sanity_check_at_startup
from src.Scans.quick import quick_scan
from src.Scans.regular import regular_scan
from src.Scans.hard import hard_scan
from src.Analyze.report import build_rapport
from src.Analyze.analyze import extract_more_Js_file_as_u_can
from src.Analyze.send_report import sendMail


def search_domains(target_domain, depth):
    """
        return une liste de domain
        quick_scan: # result in gau_solo_urls.txt subjs_url.txt hakrawler_urls.txt gospider_url.txt
        regular_scan: # result
        hard_scan: # result
    """
    print(f'Searching Domains on target(s): {target} with depth {depth}\n-------------')
    os.system(f'echo "{target_domain}" >> target.txt')
    # if depth == 1:
    domains = quick_scan(target_domain)
    # elif depth == 2:
    #     # TODO: from the result of quick scan start regular scan, using all the subdomains
    #     domains = regular_scan(target_domain)
    # else:
    #     # TODO: from the result of regular scan, search in files.js for more endpoints, than filter on subdomains
    #     domains = hard_scan(target_domain)
    if len(domains) < 1:
        print('(ERROR) no subdomain found for this target')
        exit(-1)
    else:
        print(f'(DEBUG) Finally all tools found {len(domains)} endpoints')
        build_rapport(domains)
        exit(0)
    return domains


def B4DID34():
    # TODO: setup for multiple domain, we will need it
    """ From 1 domain, search for maximum subdomain than search for JS file """
    domain, depth = sanity_check_at_startup()
    domains = search_domains(domain, depth)  # TODO: filtered by allowed scope
    jsfiles = extract_more_Js_file_as_u_can(domains)  # TODO: only in DEPTH=3, but i'm lazy

    # report = generate_report(domains, assets_found)
    # sendMail(report)


if __name__ == "__main__":
    B4DID34()
