def basic_filter_endpoint(urls):
    result = list()
    for url in urls:
        if "putass" in url:
            result.append(url)
    return result


def extract_subdomains(urls):
    """ filter port / http:// / https:// """
    results = list()
    print(f'(DEBUG) Starting to filter ({len(urls)}) urls')
    print(f'(DEBUG) Exemple of url to filter {urls[0]}')
    for url in urls:
        filtered = url.replace("http://", "").replace("https://", "").replace("ftp://", "").replace("ftps://", "")
        filtered = filtered.replace("www.", "").replace(":80", "").replace(":443", "")
        if '/' in filtered:
            filtered = filtered[0:filtered.index('/')]
        filtered = filtered[0:filtered.index('?')] if '?' in filtered else filtered
        results.append(filtered)
    results = list(set(results))
    print(f'(DEBUG) Apres filter, found domains ({len(results)})')
    print(f'(DEBUG) Exemple de domain found {results[0]}')
    return results

