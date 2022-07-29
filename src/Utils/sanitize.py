import os
from threading import Thread
from src.Utils.shell import VERBOSE, shell, dump_to_file


def check_alive_domain(domain):
    """ With httpx check if 1 domain is alive, return True or false """
    return int(shell(f"echo {domain} | httpx -silent | wc -l", verbose=False, outputOnly=True)) == 0


def check_alives_domains(nameFile, nbr_cpu=42):
    """ With httpx check if a list of domain in a file are alive, return a list of domains alives """
    domains_httpx = shell(f'httpx -l tmp-search.txt -threads {nbr_cpu} -silent', verbose=False, outputOnly=True).split('\n')
    print(f'(DEBUG) Httpx filtered domains and found {len(domains_httpx)} alives sub')
    return domains_httpx


def strip_domains(urls, tool_name=None):
    subdomain_already_know = shell(f'cat tmp-search.txt', verbose=False, outputOnly=True).split('\n')
    for url in urls:
        filtered = url.replace("http://", "").replace("https://", "").replace("ftp://", "").replace("ftps://", "")
        filtered = filtered.replace("www.", "").replace(":80", "").replace(":443", "")
        filtered = filtered[0:filtered.index('/')] if '/' in filtered else filtered
        filtered = filtered[0:filtered.index('?')] if '?' in filtered else filtered
        if filtered not in subdomain_already_know:
            if len(url) > 250:
                pass
                #print(url)
                #input(f"{tool_name}: renvoie un tableau de {len(url)}:a la place dune url")
            else:
                subdomain_already_know.append(filtered)
    return list(set(subdomain_already_know))


# TODO: YOU need to do that only after all thread are done in cycle, not at every thread end
def dont_dump_domain_two_times(domains=None, dump_file_name="tmp-search.txt"):
    """ check in tmp-search.txt for duplicate & bullshit domains, than, filter"""
    subdomain_already_know = shell(f'cat {dump_file_name}', verbose=False, outputOnly=True).split('\n')
    final_res = list()
    if domains is not None:
        for domain in domains:
            if domain not in subdomain_already_know:
                final_res.append(domain)
        os.system(f'rm -f {dump_file_name}')
        final_res = list(set(strip_domains(urls=final_res)))
    else:
        final_res = list(set(strip_domains(urls=subdomain_already_know)))
    dump_to_file(namefile=dump_file_name, lines=final_res)
    return final_res


def extract_subdomains_and_dump(urls, medium=False):
    """ filter substring in domains like / http:// / https:// and everything after '?' """

    subdomain_already_know = strip_domains(urls, tool_name="from dump it")
    dump_to_file(namefile="tmp-search.txt", mode='a', lines=subdomain_already_know)
    return subdomain_already_know


def sanity_check_at_startup():
    """
        [X] Check if target is alive
        [X] Check if all binary are present & configured
        [X] Check if all variable are present (TODO: Dynamic conf regarding the env var present)
    """
    try:
        depth = int(os.environ['DEPTH'])
        os.system('rm -f .txt')  # to clean docker volumes duplicate files
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

#
# def check_alives_domains(domains):
#     """
#         build a chunked list of domains, set to use maximum CPU in multithreads
#         result are in files and returned 2 list, 1 alive & 1 dead domains
#     """
#     print(f'(DEBUG) Checking ICMP staus for {len(domains)} domains')
#     pThreads, started, idx_current_threads = list(), list(), 0
#     nbr_cpu = 1 if (os.cpu_count() == 1 or os.cpu_count() == 2) else int(os.cpu_count() / 2)  # /2 bc dont want 100% cpu
#     list_domains_chunked = [domains[idx:idx + nbr_cpu] for idx in range(0, len(domains), nbr_cpu)]  # split into chunks
# #    [pThreads.append(Thread(target=alives_thread, args=(domains_chunk,))) for domains_chunk in list_domains_chunked]
#     for domains_chunk in list_domains_chunked:
#         pThreads.append(Thread(target=alives_thread, args=(domains_chunk, len(pThreads))))
#     print(f'(DEBUG) Starting {len(pThreads)} threads for {len(domains)} domains & {len(list_domains_chunked)} chunks')
#     for idx_threads in range(0, len(pThreads)):
#         idx_current_threads += + 1
#         started.append(idx_current_threads)
#         pThreads[idx_threads].start()  # starting maximum threads
#         try:
#             if idx_current_threads == nbr_cpu:
#                 for idx in started:
#                     print(f'(DEBUG) THREAD JOIN: {idx} thread')
#                     pThreads[started[idx]].join()
#                 #[pThreads[started[idx]].join() for idx in started]  # join threads for results befor restart if needed
#                 idx_current_threads, started = 0, list()
#         except RuntimeError as e:
#             print(idx)
#             print(e)
#     print(f'(DEBUG) All threads are finish, starting reading files')
#     alives_domains = shell('cat alives.txt', verbose=False, outputOnly=True).split('\n')
#     dead_domains = shell('cat deads.txt', verbose=False, outputOnly=True).split('\n')
#     print(f'(DEBUG) Found {len(dead_domains)} deads in deads.txt & found {len(alives_domains)} alive in alive.txt')
#     return alives_domains, dead_domains