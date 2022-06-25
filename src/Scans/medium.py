import time
from src.Scans.simple import quick_scan
from threading import Thread
from src.Utils.Shell import shell


def exec_pool_domains(pool_threads):
    [process.start() for process in pool_threads]
    [process.join() for process in pool_threads]


def regular_scan(domains):
    start = time.time()
    print(f'(DBUG) Starting MEDIUM scan with {len(domains)} domains')
    results = list()
    rcx = 0
    rdx = 0
    pThreads = list()
    for domain in domains:
        quick_scan(domain)
        rcx = rcx + 1
    # TODO: filter in files all the duplicates
    print(f'(DEBUG) Medium scan executed in {time.time() - start} seconds')
    return domains

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
