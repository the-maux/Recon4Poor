from src.Utils.Sanitize import check_alives_domains


def build_rapport(domains):
    domain_offline, domain_alive = check_alives_domains(domains)
    nbr_alives = len(domain_alive)
    print(f'(DEBUG) We found {nbr_alives} domain still alive ! {":D" if nbr_alives > 10 else ":("}')
    with open('domains.txt', 'w') as f:
        for item in domains:
            f.write(f"{item}\n")
    with open('domains-alive.txt', 'w') as f:
        for item in domain_offline:
            f.write(f"{item}\n")
    with open('domains-offline.txt', 'w') as f:
        for item in domain_alive:
            f.write(f"{item}\n")