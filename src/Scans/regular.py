from src.Scans.quick import quick_scan
from threading import Thread


def regular_scan(domains):
    print(f'(DBUG) Starting regular scan with {len(domains)} domains')
    results = list()
    pThreads = list()
    for domain in domains:
        pThreads.append(Thread(target=quick_scan, args=(domain,)))
    [process.start() for process in pThreads]
    [process.join() for process in pThreads]
    stdout, stderr, returncode = shell('cat tmp-search.txt', verbose=False)
    return results