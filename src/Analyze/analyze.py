from src.Analyze.send_report import sendMail
from src.Utils.Shell import shell
from src.Utils.Sanitize import extract_subdomains_and_dump


def search_JS_files_in_one_domain(domain):
    listOfJsFilesPath = list()
    # Using subjs
    cmd = 'cat listOfDomains.txt | gau -subs -b png,jpg,jpeg,html,txt,JPG | subjs  |  '
    cmd = cmd + "awk -F '\?' '{print $1}' | sort -u > subjs_url.txt"
    stdout, stderr, returncode = shell(cmd, verbose=True)
    print("(INFO) subjs individually found: $(cat subjs_url.txt | wc -l) url(s)")

    # Using JsSubfinder
    cmd = 'jsubfinder -f listOfDomains.txt  > jsubfinder.txt'
    stdout, stderr, returncode = shell(cmd, verbose=True)
    print("(INFO) jsubfinder individually found: $(cat jsubfinder.txt | wc -l) url(s)")

    # Using hakrawler
    cmd = 'cat listOfDomains.txt | hakrawler -js -depth 2 -scope subs -plain >> hakrawler_urls.txt'
    stdout, stderr, returncode = shell(cmd, verbose=True)
    print("(INFO) hakrawler individually found: $(cat hakrawler_urls.txt | wc -l) url(s)")
    return listOfJsFilesPath


def extract_JsFiles_From_endpoint(endpoints):
    """ Use tool to extract maximum Js file from a list of endpoints """
    jsfilesPath = list()
    for endpoint in endpoints:
        pass
    return endpoints


def extract_endpoints_From_domain(domain):
    """ Use a tool to extract maximum endpoints from domain """
    endpoints = list()
    return endpoints


def extract_more_Js_file_as_u_can(domains):
    """
        Search in list of domains, first all endpoints from domains than extract JS files from it
        :return: listof filtered urls to uniq JS files
    """
    pathOfJsFilesFound = list()
    for domain in domains:  # TODO: Thread it
        print(f'DEBUG) [+] Started gathering Js files from domain({domain}) and path found')
        endpoints = extract_endpoints_From_domain(domain=domain)
        pathOfJsFilesFound.append(extract_JsFiles_From_endpoint(endpoints))
    return pathOfJsFilesFound


def searching_assets(results):
    """ Santinize the results before the final report """
    results = list()
    sendMail(results)
    return results
