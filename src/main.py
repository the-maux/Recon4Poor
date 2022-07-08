import os, time
from src.Utils.Sanitize import sanity_check_at_startup, check_alives_domains
from src.Scans.simple import quick_scan
from src.Scans.medium import medium_scan
from src.Analyze.report import dump_domains_state
from src.Utils.Shell import shell
from src.Analyze.analyze import search_JSfiles_in_file


def search_domains(target_domain, depth):
    """
        return: list of domains
        quick_scan(depth1): just a quick scan, no JS analyse
        regular_scan(depth2): Analyse Twice with the second time in inut the subdomain
        hard_scan(depth3): Start from regular_scan & download all JS files to scan for new subdomains
    """
    print(f'Searching Domains on target(s): {target_domain} with depth {depth}\n-------------')
    if depth == 1:
        domains = quick_scan(target_domain)
    elif depth >= 2:
        quick_scan(target_domain)
        domains = medium_scan()
    else:
        domains = list()
        # with open('tmp-search-medium.txt', 'r') as f:
            # print("DUMPING MEDIUM SCAN   ! ")
            # domains = f.read().splitlines()
            # for line in domains:
            #     print(line)
            # print(f"Found with medium scan: {len(domains)}")
    # if len(domains) < 1:
    #     print('(ERROR) no subdomain found for this target')
    #     exit(-1)
    # else:
    #     print(f'(DEBUG) Finally all tools found {len(domains)} domains')
    #     exit(0)
    return domains


def B4DID34T(domains=None):
    # TODO: setup for multiple domain, we will need it
    """ From 1 domain, search for maximum subdomain than search for JS file """
    start = time.time()
    if domains is None:
        domain, depth = sanity_check_at_startup()
        domains = search_domains(domain, 2)  # TOFIX: when DEPTH  is at 1, you do twice check_alives_domains
        domain_alive = check_alives_domains(domains)
        dump_domains_state(domains, domain_alive)
    print(f'(DEBUG) Execution success in {int(time.time() - start)} seconds !')
# if depth > 3:  # TODO: in cas of depth == 3 add the gospider use
#     jsfiles = search_JSfiles_in_file(file_domains='domains-alive.txt')
#     # TODO: once the path JSfile found, downloads them
#     # TODO: once all JSFile found, scan them, and search for endpoints / new subdomains
#     # TODO: and restart for a secret DEPT=4
# # sendMail(report) # TODO: at least push to Gmail & Slack


if __name__ == "__main__":
    print('LOADING')
    B4DID34T()
