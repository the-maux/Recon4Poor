import os
from src.Utils.Sanitize import sanity_check_at_startup, check_alives_domains
from src.Scans.quick import quick_scan
from src.Scans.regular import regular_scan
from src.Analyze.report import dump_domains_state
from src.Analyze.analyze import search_JSfiles_in_file


def search_domains(target_domain, depth):
    """
        return: list of domains
        quick_scan(depth1): just a quick scan, no JS analyse
        regular_scan(depth2): Analyse Twice with the second time in inut the subdomain
        hard_scan(depth3): Start from regular_scan & download all JS files to scan for new subdomains
    """
    print(f'Searching Domains on target(s): {target_domain} with depth {depth}\n-------------')
    domains = quick_scan(target_domain)
    if depth >= 2:
        # TODO: from the result of quick scan start regular scan, using all the subdomains
        domains = regular_scan(domains)
    # else:
    #     # TODO: from the result of regular scan, search in files.js for more endpoints, than filter on subdomains
    #     domains = hard_scan(target_domain)
    if len(domains) < 1:
        print('(ERROR) no subdomain found for this target')
        exit(-1)
    else:
        print(f'(DEBUG) Finally all tools found {len(domains)} domains')
        exit(0)
    return domains


def B4DID34T(domains=None):
    # TODO: setup for multiple domain, we will need it
    """ From 1 domain, search for maximum subdomain than search for JS file """
    if domains is None:
        domain, depth = sanity_check_at_startup()
        domains = search_domains(domain, depth)  # TOFIX: when DEPTH  is at 1, you do twice check_alives_domains
        domain_alive = check_alives_domains(domains)
        dump_domains_state(domains, domain_alive)
        os.system('ls -l')

# if depth > 3:  # TODO: in cas of depth == 3 add the gospider use
#     jsfiles = search_JSfiles_in_file(file_domains='domains-alive.txt')
#     # TODO: once the path JSfile found, downloads them
#     # TODO: once all JSFile found, scan them, and search for endpoints / new subdomains
#     # TODO: and restart for a secret DEPT=4
# # sendMail(report) # TODO: at least push to Gmail & Slack


if __name__ == "__main__":
    B4DID34T()
