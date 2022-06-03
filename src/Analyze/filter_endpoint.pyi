def basic_filter_endpoint(urls):
    result = list()
    for url in urls:
        if "" in url:
    return result

def filter_all(urls):
    """ filter port / http:// / https://
    """
    results = list()
    for url in urls:
        filtered = url.replace("http://", "").replace("https://", "").replace(":80", "").replace(":443", "")
        try:
            filtered = filtered[0:filtered.index('?')]
        except ValueError:
            pass
        results.append(filtered)
    return list(set(results))


def build_path_tree_from_urls(urls):
    tree = dict()
    return tree


def extract_subdomains_from_tree(tree):
    subdomains = list()
    return subdomains

def give_me_real_endpoint(urls):
    urls = filter_all(urls)
    tree = build_path_tree_from_urls(urls)
    subdomains = extract_subdomains_from_tree(tree)
    return urls
