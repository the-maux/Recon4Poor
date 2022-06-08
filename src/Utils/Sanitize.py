import os
from src.Utils.Shell import VERBOSE


def final_sanityze(domains):
    """ Test a list of domains to check if they respond """
    domain_alive = list()
    domain_offline = list()
    for domain in domains:
        response = os.system(f"ping -c 1 {domain}")
        if response == 0:
            domain_alive.append(domain)
        else:
            domain_offline.append(domain)
    return domain_offline, domain_alive


def extract_subdomains(urls):
    """ filter substring in domains like / http:// / https:// and everything after '?' """
    results = list()
    for url in urls:
        filtered = url.replace("http://", "").replace("https://", "").replace("ftp://", "").replace("ftps://", "")
        filtered = filtered.replace("www.", "").replace(":80", "").replace(":443", "")
        if '/' in filtered:
            filtered = filtered[0:filtered.index('/')]
        filtered = filtered[0:filtered.index('?')] if '?' in filtered else filtered
        results.append(filtered)
    results = list(set(results))
    print(f'(DEBUG) After filtering, found ({len(results)}) domains')
    return results


def sanity_check_at_startup():
    """
        [X] Check if target is alive
        [X] Check if all binary are present & configured
        [X] Check if all variable are present (TODO: Dynamic conf regarding the env var present)
    """
    try:
        depth = int(os.environ['DEPTH'])
        if VERBOSE:
            print(f'(DEBUG) DEPTH analyse was not set, default is {os.environ["DEPTH"]}')
    except Exception:
        if VERBOSE:
            print('(WARNING) DEPTH analyse was not set, default is 1')
        depth = 1
    try:
        target = os.environ['TARGET']
        return target, depth
    except Exception as e:
        print(f'(ERROR) You need to set at least the var env $TARGET: {e}')
        exit(-1)
