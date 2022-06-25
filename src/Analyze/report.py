from src.Utils.Shell import dump_to_file


def dump_domains_state(domains, domain_alive):
    print(f'(DEBUG) Final check to filter on alive hosts for {len(domains)} subdomains')
    nbr_alives = len(domain_alive)
    print(f'(DEBUG) We found {nbr_alives} domain still alive ! {":D" if nbr_alives > 10 else ":("}')
    dump_to_file(namefile='domains.txt', mode='w', lines=domains)
    dump_to_file(namefile='domains-alive.txt', mode='w', lines=domain_alive)
