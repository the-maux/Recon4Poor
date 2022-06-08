from src.Utils.Sanitize import final_sanityze


def build_rapport(domains):
    domains_offline, domains_alive = final_sanityze(domains)
    with open('domains.txt', 'w') as f:
        for item in domains:
            f.write(f"{item}\n")
    with open('domains-alive.txt', 'w') as f:
        for item in domains_offline:
            f.write(f"{item}\n")
    with open('domains-offline.txt', 'w') as f:
        for item in domains_alive:
            f.write(f"{item}\n")