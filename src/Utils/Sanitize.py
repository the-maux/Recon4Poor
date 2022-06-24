import os
from threading import Thread
from src.Utils.Shell import VERBOSE, shell, dump_to_file

# def alives_thread(domains_chunk):
#     domain_alive, domain_offline, rcx = list(), list(), 0
#     for domain in domains_chunk:
#         stdout, stderr, code = shell(f"ping -c 1 {domain}", verbose=False)
#         if code == 0:
#             os.system(f"ping -c 1 {domain} && echo {domain} >> alives.txt  || echo {domain} >> dead.txt")
#             domain_alive.append(domain)
#             rcx = rcx + 1
#         else:
#             domain_offline.append(domain)
#     print(f'(DEBUG) ICMP Result is  {len(domain_alive)} alive & {len(domain_offline)} offlines')


def alives_thread(domains_chunk, thread_nbr='???'):
#    domain_alive, domain_offline, rcx = list(), list(), 0
    for domain in domains_chunk:
        os.system(f"ping -c 1 {domain} && echo {domain} >> alives.txt  || echo {domain} >> deads.txt")
    print(f'(DEBUG) Thread-{thread_nbr} is ending')
    os.system("ls -l")


def check_alives_domains(domains):
    """
        build a chunked list of domains, set to use maximum CPU in multithreads
        result are in files and returned 2 list, 1 alive & 1 dead domains
    """
    print(f'(DEBUG) Checking ICMP staus for {len(domains)} domains')
    pThreads, started, idx_current_threads = list(), list(), 0
    nbr_cpu = 1 if (os.cpu_count() == 1 or os.cpu_count() == 2) else int(os.cpu_count() / 2)  # /2 bc dont want 100% cpu
    list_domains_chunked = [domains[idx:idx + nbr_cpu] for idx in range(0, len(domains), nbr_cpu)]  # split into chunks
#    [pThreads.append(Thread(target=alives_thread, args=(domains_chunk,))) for domains_chunk in list_domains_chunked]
    for domains_chunk in list_domains_chunked:
        pThreads.append(Thread(target=alives_thread, args=(domains_chunk, len(pThreads))))
    print(f'(DEBUG) Starting {len(pThreads)} threads for {len(domains)} domains & {len(list_domains_chunked)} chunks')
    for idx_threads in range(0, len(pThreads)):
        idx_current_threads += + 1
        started.append(idx_current_threads)
        pThreads[idx_threads].start()  # starting maximum threads
        try:
            if idx_current_threads == nbr_cpu:
                for idx in started:
                    print(f'(DEBUG) THREAD JOIN: {idx} thread')
                    pThreads[started[idx]].join()
                #[pThreads[started[idx]].join() for idx in started]  # join threads for results befor restart if needed
                idx_current_threads, started = 0, list()
        except RuntimeError as e:
            print(idx)
            print(e)
    print(f'(DEBUG) All threads are finish, starting reading files')
    alives_domains = shell('cat alives.txt', verbose=False, outputOnly=True).split('\n')
    dead_domains = shell('cat deads.txt', verbose=False, outputOnly=True).split('\n')
    print(f'(DEBUG) Found {len(dead_domains)} deads in deads.txt & found {len(alives_domains)} alive in alive.txt')
    return alives_domains, dead_domains


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
