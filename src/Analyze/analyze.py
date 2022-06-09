from src.Utils.Shell import shell


def search_JSfiles_in_file(file_domains):
    listOfJsFilesPath = list()
    # Using subjs
    cmd = f'cat {file_domains} | gau -subs -b png,jpg,jpeg,html,txt,JPG | subjs  |  '
    cmd = cmd + "awk -F '\?' '{print $1}' | sort -u > subjs_url.txt"
    stdout, stderr, returncode = shell(cmd, verbose=True)
    print("(INFO) subjs individually found: $(cat subjs_url.txt | wc -l) url(s)")

    # Using JsSubfinder
    cmd = f'jsubfinder -f {file_domains}  > jsubfinder.txt'
    stdout, stderr, returncode = shell(cmd, verbose=True)
    print("(INFO) jsubfinder individually found: $(cat jsubfinder.txt | wc -l) url(s)")

    # Using hakrawler
    cmd = f'cat {file_domains} | hakrawler -js -depth 2 -scope subs -plain > hakrawler_urls.txt'
    stdout, stderr, returncode = shell(cmd, verbose=True)
    print("(INFO) hakrawler individually found: $(cat hakrawler_urls.txt | wc -l) url(s)")
    return listOfJsFilesPath