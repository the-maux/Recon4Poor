import os
from threading import Thread
from src.Utils.Shell import VERBOSE, shell, dump_to_file


def check_alive_domain(domain):
    """ With httpx check if 1 domain is alive, return True or false """
    return int(shell(f"echo {domain} | httpx -silent | wc -l", verbose=False, outputOnly=True)) == 0


def check_alives_domains(nameFile, nbr_cpu=42):
    """ With httpx check if a list of domain in a file are alive, return a list of domains alives """
    domains_httpx = shell(f'httpx -l {nameFile} -threads {nbr_cpu} -silent', verbose=False, outputOnly=True).split('\n')
    print(f'(DEBUG) Httpx filtered domains and found {len(domains_httpx)} alives sub')
    return domains_httpx


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


def sanity_check_at_startup():
    """
        [X] Check if target is alive
        [X] Check if all binary are present & configured
        [X] Check if all variable are present (TODO: Dynamic conf regarding the env var present)
    """
    try:
        depth = int(os.environ['DEPTH'])
    except Exception:
        depth = 1
    if VERBOSE:
        print(f'(INFO) DEPTH analyse is {depth}')
    try:
        target = os.environ['TARGET']
        return target, depth
    except Exception as e:
        print(f'(ERROR) You need to set at least the var env $TARGET: {e}')
        exit(-1)
