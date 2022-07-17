import time
from src.Scans.quick import quick_scan
from src.Utils.sanitize import dont_dump_domain_two_times
from threading import Thread
from src.Utils.shell import shell


def exec_pool_domains(pool_threads):
    [process.start() for process in pool_threads]
    [process.join() for process in pool_threads]


def medium_scan(domains):
    """ After a first quick scan, re-doit with every possible subdomain founds, results are in """
    print(f'(DBUG) Starting MEDIUM scan with {len(domains)} domains')
    rcx, results, start = 0, list(), time.time()
    for domain in domains[0:5]:  # TOREMOVE !!!
        print(f'(DEBUG) Medium search for  {domain} domains')
        subsubdomains_found = quick_scan(domain, medium=True)
        results = list(set(subsubdomains_found + results))
        rcx = rcx + 1
        print(f'(DEBUG) Medium tread-{rcx} end with {len(subsubdomains_found)} domains')
    print(f'(DEBUG) Medium scan executed in {time.time() - start} seconds')
    return results


def medium_scan_threads(domains):
    """ Build a thread Queu and filter the results to intense scan on subsubdomain """
    print(f'(DBUG) Starting MEDIUM scan with {len(domains)} domains')
    rcx, pThreads = 0, list()
    for domain in domains:
        pThreads.append(Thread(target=quick_scan, args=(domain,)))
        rcx = rcx + 1
        if rcx == 2: # mannualy putting number of thread
            print(f'(DEBUG) Starting pools of domains: {rcx}')
            exec_pool_domains(pThreads)
            rcx, pThreads = 0, list()
            dont_dump_domain_two_times(dump_file_name='', )
            input('On relance gros ? ')
    return domains
