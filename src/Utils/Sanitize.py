import os


def sanitize_my_domain(urls_lists):
    """
        #TODO: before returning list of urls, check if urls are alive (maybe check dup file too, or already Analyzed ?)
        take a list of urls in input, and check them to remove the dead one or useless
        cat SubDomainizer.txt | sed 's$https://$$' | sed 's$www.$$' | sort -u > listOfDomains.txt
    """
    return urls_lists


def sanity_check_at_startup():
    """
        Check if target is alive
        Check if all binary are present & configured
        Check if all variable are present (TODO: Dynamic conf regarding the env var present)
    """
    try:
        target = os.environ['TARGET']
        depth = os.environ['DEPTH']
        return target, depth
    except Exception:
        exit(-1)
