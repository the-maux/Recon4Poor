import os
from src.Utils.Shell import VERBOSE, shell, dump_to_file


def check_alives_domains(domains):
    """ Test a list of domains to check if they respond """
    print(f'(INFO) Checking ICMP staus for {len(domains)}')
    domain_alive = list()
    domain_offline = list()
    rcx = 0
    for domain in domains:
        stdout, stderr, code = shell(f"ping -c 1 {domain}", verbose=False)
        if code == 0:
            domain_alive.append(domain)
            rcx = rcx + 1
        else:
            domain_offline.append(domain)
    print(f'(DEBUG) ICMP Result is  {len(domain_alive)} alive & {len(domain_offline)} offlines')
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
        dump_to_file(namefile='tmp-search.txt', mode='a', lines=results)
    return results


def check_if_target_is_alive(target):
    stdout, stderr, code = shell(f"ping -c 1 {target}", verbose=False)
    if code != 0:
        print('(WARNING) TARGET IS OFFLINE')
    return code == 0


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
            print('(INFO) DEPTH analyse was not set, default is 2')
        depth = 2
    try:
        target = os.environ['TARGET']
        check_if_target_is_alive(target)
        return target, depth
    except Exception as e:
        print(f'(ERROR) You need to set at least the var env $TARGET: {e}')
        exit(-1)
