from src.Analyze.send_report import sendMail
from src.Utils.Sanitize import sanitize_my_domain


def search_endpoint(list_urls_toJsFile):
    """
        Search in Js File, all endpoint
        # TOKNOW: linkfinder doesnt work if "https" is not present
    """
    listOfEndpoints = list()
    # cat all_js_files_found.txt | sed 's$https://$$' | awk '{print "https://" $0}' > search_endpoint.txt # tobe sur there are alway a https://
    # interlace -tL search_endpoint.txt -threads 5 -c "python3 ./tools/LinkFinder/linkfinder.py -d -i '_target_' -o cli >> all_endpoints.txt" --silent --no-bar
    number_of_endpoint_found = 42  # $(cat all_endpoints.txt | wc -l)
    print("(INFO) Number of endpoint found with LinkFinder: $(cat endpoints.txt | wc -l)")
    return listOfEndpoints  # need to be filtered for scope / domain / interest


def search_JS_files(domains):
    """
        Search in list of urls, all JS files
        :return: listof filtered urls to uniq JS files
    """
    print('DEBUG) [+] Started gathering Js files from domain and path found')
    listOfJsFiles = list()

    # Using subjs
    # cat listOfDomains.txt | gau -subs -b png,jpg,jpeg,html,txt,JPG | subjs  |  awk -F '\?' '{print $1}' | sort -u > subjs_url.txt
    print("(INFO) subjs individually found: $(cat subjs_url.txt | wc -l) url(s)")


    # Using JsSubfinder
    # jsubfinder -f listOfDomains.txt  > jsubfinder.txt
    print("(INFO) jsubfinder individually found: $(cat jsubfinder.txt | wc -l) url(s)")


    # Using hakrawler
    # cat listOfDomains.txt | hakrawler -js -depth 2 -scope subs -plain >> hakrawler_urls.txt
    print("(INFO) hakrawler individually found: $(cat hakrawler_urls.txt | wc -l) url(s)")

    return sanitize_my_domain(listOfJsFiles)


def analyse_result(results):
    """ Santinize the results before the final report """
    results = list()
    sendMail(results)
    return results

