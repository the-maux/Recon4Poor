import time
from src.Utils.sanitize import sanity_check_at_startup, check_alives_domains
from src.Utils.send_report import dump_domains_state, sendMail
from src.Utils.shell import dump_to_file
from src.Scans.quick import quick_scan
from src.Scans.medium import medium_scan, medium_scan_threads


def search_domains(target_domain, depth):
    """
        return: list of domains
        quick_scan(depth1): just a quick scan, no JS analyse
        regular_scan(depth2): Analyse Twice with the second time in input the subsubdomain
        hard_scan(depth3): Start from regular_scan & download all JS files to scan for new subdomains
    """
    print(f'Searching Domains on target(s): {target_domain} with depth {depth}\n-------------')
    if depth == 1:
        domains = quick_scan(target_domain)
        dump_to_file(namefile='quick-1.txt', lines=domains)
    elif depth >= 2:
        domains = quick_scan(target_domain)
        dump_to_file(namefile='quick-1.txt', lines=domains)
        domains = medium_scan_threads(domains)
        dump_to_file(namefile='medium-2.txt', lines=domains)
    else:
        domains = list()
    # if len(domains) < 1:
    #     print('(ERROR) no subdomain found for this target')
    #     exit(-1)
    # else:
    #     print(f'(DEBUG) Finally all tools found {len(domains)} domains')
    #     exit(0)
    return domains


def B4DID34(domains=None):
    # TODO: setup for multiple domain, we will need it
    """ From 1 domain, search for maximum subdomain than search for JS file """
    start = time.time()
    if domains is None:
        domain, depth = sanity_check_at_startup()
        domains = search_domains(domain, depth=2)  # TOFIX: when DEPTH  is at 1, you do twice check_alives_domains
        domain_alive = check_alives_domains(domains)
        dump_domains_state(domains, domain_alive)
    print(f'(DEBUG) Execution success in {int(time.time() - start)} seconds !')
    #sendMail(report) # TODO: at least push to Gmail & Slack


if __name__ == "__main__":
    B4DID34()
