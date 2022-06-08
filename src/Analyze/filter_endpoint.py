def basic_filter_endpoint(urls):
    result = list()
    for url in urls:
        if "Find interesting Subdomains" not in url and \
                "____) | |_| | |_) | |__| | (_) | | | | | | (_| | | | | | |" not in url:
            result.append(url)
    return result


def final_sanityze(urls):
    # TODO: check si le domain répond d'un point de vue network
    return urls


def extract_subdomains(urls):
    """ filter port / http:// / https:// """
    results = list()
    for url in urls:
        filtered = url.replace("http://", "").replace("https://", "").replace("ftp://", "").replace("ftps://", "")
        filtered = filtered.replace("www.", "").replace(":80", "").replace(":443", "")
        if '/' in filtered:
            filtered = filtered[0:filtered.index('/')]
        filtered = filtered[0:filtered.index('?')] if '?' in filtered else filtered
        results.append(filtered)
    results = list(set(results))
    print(f'(DEBUG) After filtering, found ({len(results)}) domains')
    return results

