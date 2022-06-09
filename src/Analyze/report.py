from src.Utils.Sanitize import check_alives_domains
from src.Utils.Shell import dump_to_file


def build_rapport(domains):
    print(f'(DEBUG) Final check to filter on alive hosts for {len(domains)} subdomains')
    domain_offline, domain_alive = check_alives_domains(domains)
    nbr_alives = len(domain_alive)
    print(f'(DEBUG) We found {nbr_alives} domain still alive ! {":D" if nbr_alives > 10 else ":("}')
    dump_to_file(namefile='domains.txt', mode='w', lines=domains)
    dump_to_file(namefile='domains-alive.txt', mode='w', lines=domain_alive)
    dump_to_file(namefile='domains-offline.txt', mode='w', lines=domain_offline)
