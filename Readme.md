Combine multiple tools to search subdomain in a efficient way, runnable externaly in C.I or external VPS.

### Usage

#### Usage with from GithubActions
    - Fork the project
    - Go to the project settings and set the varriables (TARGET, DEPTH & GMAIL_TOKEN)
    - Run the actions (or push a commit with a message start with "SCAN" :)

#### Local usage:
Result will be in results.txt
``` shell
    git pull origin develop
    docker build recoon4poor:latest . && docker run -e TARGET=$TARGET recoon4poor:ltest
```

:warning: Working on Linux & Mac OS X versions only 

Image is hosted directly under ghcr.io/the-maux/recoon4poor:latest
So you can just do a 
```` shell
id
docker run -e TARGET=foo.com recoon4poor:latest
````
TODO: Put a graphic with tools comparaison
TODO: explain difference with the multiples DEPTH and usae of GMAIL_TOKEN
TODO: Gif exemple of an execution

Thanks to all the makers <3 :
- https://github.com/nsonaniya2010/SubDomainizer
- https://github.com/aboul3la/Sublist3r
- https://github.com/duty1g/subcat
- https://github.com/m4ll0k/SecretFinder
- https://github.com/GerbenJavado/LinkFinder
- https://github.com/projectdiscovery/subfinder
- https://github.com/lc/gau
- https://github.com/projectdiscovery/httpx
- https://github.com/tomnomnom/assetfinder
- https://github.com/jaeles-project/gospider
- https://github.com/tomnomnom/waybackurls
- https://github.com/ThreatUnkown/jsubfinder
- https://github.com/hakluke/hakrawler

#### Inspired by KathanP19 in bash & Go: https://github.com/KathanP19/JSFScan.sh
https://medium.com/@sherlock297/how-to-check-subdomains-are-active-or-not-91fd75e3e412
