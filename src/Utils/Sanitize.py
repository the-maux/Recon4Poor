import os
from src.Utils.Shell import VERBOSE, shell


def final_sanityze(domains):
    """ Test a list of domains to check if they respond """
    domain_alive = list()
    domain_offline = list()
    rcx = 0
    for domain in domains:
        stdout, stderr, code = shell(f"ping -c 1 {domain}", verbose=False)
        if code == 0:
            print(f'(INFO) {domain} IS ONLINE !')
            domain_alive.append(domain)
            rcx = rcx + 1
        else:
            print(f'(INFO) {domain} IS DEAD :( !')
            domain_offline.append(domain)
    print(f'(DEBUG) We found {rcx} domain still alive !')
    return domain_offline, domain_alive


def extract_subdomains_and_dump(urls, dump=True):
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
    if dump is True:
        with open('tmp-search.txt', 'a') as f:
            for item in results:
                f.write(f"{item}\n")
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
