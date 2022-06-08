def basic_filter_endpoint(urls):
    result = list()
    for url in urls:
        if "putass" in url:
            result.append(url)
    return result


def filter_all(urls):
    """ filter port / http:// / https://
    """
    results = list()
    print(f'(DEBUG) Starting to filter ({len(urls)}) urls')
    print(f'(DEBUG) Exemple of url to filter {urls[0]}')
    for url in urls:
        filtered = url.replace("http://", "").replace("https://", "").replace(":80", "").replace(":443", "")
        filtered = filtered.replace("www.", "")
        if '/' in filtered:
            filtered = filtered[0:filtered.index('/')]
        filtered = filtered[0:filtered.index('?')] if '?' in filtered else filtered
        results.append(filtered)
    results = list(set(results))
    print(f'(DEBUG) Apres le filtre, Returning urls ({len(results)})')
    print(f'(DEBUG) Exemple of url que lon revnoi {urls[0]}')
    return results


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
