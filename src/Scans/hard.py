

def hitme():
    print(f'[+] Searching JsFiles-links mixing gau & subjs & assetfinder')
#   cat target.txt | sed 's$https://$$' | chaos -silent | waybackurls | httpx -silent > chaos.txt
#   TOOLONG: xargs -I@ -P20 sh -c 'gospider -a -s "@" -d 2' | grep -Eo "(http|https)://[^/"].*.js+" | sed "s#] > chaos.txt #TODO add in all urls.txt
    print("(INFO) chaos + wayback found: $(cat chaos.txt | wc -l) url(s)")


#   Removing hakrawler, cause its take too long for github actions ... more than 6hours :(
#   cat target.txt | hakrawler -js -plain -usewayback -depth 3 -scope subs | unew > hakrawlerHttpx.txt
    print("(INFO) hakrawler + wayback found: $(cat hakrawlerHttpx.txt | wc -l) url(s)")

#   cat target.txt | sed 's$https://$$' | assetfinder -subs-only | httpx -timeout 3 -threads 300 --follow-redirects -silent | sort -u > assetfinder_urls.txt
#   TOLONG: | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | awk '{print $3}' | grep -E "\.js(?:onp?)?$" |

#   TOKNOW: gospider is not working good without the "https://"
#   gospider -a -w -r -S target.txt -d 3 | grep -Eo "(http|https)://[^/\"].*\.js+" | sed "s#\] \- #\n#g" > gospider_url.txt
    print("(INFO) gospider individually found: $(cat gospider_url.txt | wc -l) url(s)")
#   contat(gospider_url.txt  + hakrawlerHttpx.txt


def regroup_found_and_filter():
    # cat all_js_files_found.txt | httpx -follow-redirects -status-code -silent | grep "[200]" | cut -d ' ' -f1 > urls_alive.txt
    # filtering duplicate & libs with no impact
    # cat all_js_files_found.txt | awk -F '?' '{ print $1 }' | grep -v "jquery" | grep $(cat target.txt | sed 's$https://$$') | sort -u > urls.txt
    #cat urls.txt | grep $(cat target.txt | sed 's$https://$$') > urls_filter.txt  # Only take if target domain is present
    #number_of_file_found_post_filter=$(cat urls_filter.txt | wc -l)
    return 42


def hard_scan(target):
    print('(DEBUG) Starting brutal scan')
    results = list()
    return results