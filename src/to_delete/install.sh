#!/usr/bin/env bash
#
#apt -yqq update  && apt -yqq install python3 python3-pip wget git unzip nano iputils-ping
#apt-get clean && ln -s /usr/bin/python3 /usr/bin/python
#
#
### Install Python lib
#git clone https://github.com/nsonaniya2010/SubDomainizer && pip install -r SubDomainizer/requirements.txt
#git clone https://github.com/aboul3la/Sublist3r && pip install -r Sublist3r/requirements.txt
#git clone https://github.com/duty1g/subcat && pip install -r subcat/requirements.txt
#git clone https://github.com/m4ll0k/SecretFinder && pip install -r SecretFinder/requirements.txt
##git clone https://github.com/GerbenJavado/LinkFinder.git && cd ./LinkFinder && python setup.py install && cd -

# Recoon Go tool
#CMD=`uname -a`
#
#if [[ "$CMD" == *"arm64"* || "$CMD" == *"aarch64"* ]]; then
#    echo "(DEBUG) arm64 platform')"
#    wget -q https://go.dev/dl/go1.18.3.linux-arm64.tar.gz && tar -C /usr/local -xzf go1.18.3.linux-arm64.tar.gz
#elif [[ "$CMD" == *"amd64"* ]]; then
#    echo "(DEBUG) amd64 platform')"
#    wget -q https://go.dev/dl/go1.18.3.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.18.3.linux-amd64.tar.gz
#else
#  echo "(DEBUG) Can't determine version of go for the platform'): $CMD"
#fi
#
#ln -s /usr/local/go/bin/go /usr/bin/go
#
#git clone https://github.com/projectdiscovery/httpx && cd httpx && make build &&
#  mv httpx /usr/bin/httpx && cd -
#
#git clone https://github.com/projectdiscovery/subfinder && cd subfinder/v2 && make build &&
#  mv subfinder /usr/bin/subfinder && cd -
#
#git clone https://github.com/lc/gau && cd gau && go mod download && go build -o ./build/gau ./cmd/gau &&
#  mv $APP_PATH/gau/build/gau /usr/bin/gau && cd -
#
## TO-FIX: because of https://github.com/tomnomnom/waybackurls/issues/41
#git clone https://github.com/tomnomnom/waybackurls && # go install github.com/tomnomnom/waybackurls@latest
#  cd waybackurls && go build main.go && mv $APP_PATH/waybackurls/main /usr/bin/waybackurls && cd -
#
#git clone https://github.com/ThreatUnkown/jsubfinder &&
#  cd jsubfinder && go build main.go && mv $APP_PATH/jsubfinder/main /usr/bin/jsubfinder
#
##go install github.com/hakluke/hakrawler@latest
#git clone https://github.com/hakluke/hakrawler &&
#  cd hakrawler && go build && mv $APP_PATH/hakrawler/hakrawler /usr/bin/hakrawler && cd -
#
#
#rm -Rf *.zip *.gz* *.md *.tgz Dockerfile Release LICENSE install.sh
#rm -Rf hakrawler jsubfinder waybackurls subfinder httpx

#  wget -q wget https://github.com/jaeles-project/gospider/releases/download/v1.1.6/gospider_v1.1.6_linux_x86_64.zip &&
#    unzip gospider_v1.1.6_linux_x86_64.zip && mv gospider_v1.1.6_linux_x86_64/gospider /usr/bin/gospider
#
#  wget -q https://github.com/lc/subjs/releases/download/v1.0.1/subjs_1.0.1_linux_amd64.tar.gz &&
#    tar -xf subjs_1.0.1_linux_amd64.tar.gz && mv subjs  /usr/bin/subjs
