import time
from src.Scans.simple import quick_scan
from src.Utils.Sanitize import extract_subdomains_and_dump, check_alives_domains
from threading import Thread
from src.Utils.Shell import shell


def exec_pool_domains(pool_threads):
    [process.start() for process in pool_threads]
    [process.join() for process in pool_threads]


def medium_scan():
    """ After a first quick scan, re-doit with every possible subdomain founds, results are in """
    domains = shell(f'cat tmp-search.txt', verbose=False, outputOnly=True).split('\n')
    print(f'(DBUG) Starting MEDIUM scan with {len(domains)} domains')
    rcx, results, start = 0, list(), time.time()
    for domain in domains[0:5]:  # TOREMOVE !!!
        print(f'(DEBUG) Medium search for  {domain} domains')
        subdomains_found = quick_scan(domain, medium=True)
        results = list(set(subdomains_found + results))
        rcx = rcx + 1
        print(f'(DEBUG) Medium tread-{rcx} end with {len(subdomains_found)} domains')
    print(f'(DEBUG) Medium scan executed in {time.time() - start} seconds')
    return results

# def regular_scan(domains):
#     print(f'(DBUG) Starting MEDIUM scan with {len(domains)} domains')
#     results = list()
#     rcx = 0
#     rdx = 0
#     pThreads = list()
#     for domain in domains:
#         pThreads.append(Thread(target=quick_scan, args=(domain,)))
#         rcx = rcx + 1
#         if rcx == 5:
#             print(f'(DEBUG) Starting pools of domains: {rcx}')
#             exec_pool_domains(pThreads)
#             pThreads = list()
#             rcx = 0
#             input('On relance gros ? ')
#     return domains
