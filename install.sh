#!/usr/bin/env bash

apt -yqq update &> nooutput && apt -yqq install python3 python3-pip wget git unzip nano iputils-ping &> nooutput
apt-get clean && ln -s /usr/bin/python3 /usr/bin/python &> nooutput


## Install python ressources for recon
git clone https://github.com/nsonaniya2010/SubDomainizer.git && pip3 install -r SubDomainizer/requirements.txt &> nooutput
git clone https://github.com/aboul3la/Sublist3r.git && pip install -r Sublist3r/requirements.txt &> nooutput
git clone https://github.com/duty1g/subcat && pip install -r subcat/requirements.txt &> nooutput

## Install python ressources Analyze files
git clone https://github.com/m4ll0k/SecretFinder.git && cd SecretFinder && pip install -r requirements.txt && cd - &> nooutput
git clone https://github.com/GerbenJavado/LinkFinder.git && cd ./LinkFinder && python3 setup.py install && cd - &> nooutput

# Recoon Go tool
CMD=`uname -a`
if [[ "$CMD" == *"arm64"* || "$CMD" == *"aarch64"* ]]; then
  echo "(DEBUG) arm64 platform')"
  wget -q https://go.dev/dl/go1.18.3.linux-arm64.tar.gz && tar -C /usr/local -xzf go1.18.3.linux-arm64.tar.gz
  # go install github.com/tomnomnom/assetfinder@latest but not working on arm64t
elif [[ "$CMD" == *"amd64"* ]]; then
  echo "(DEBUG) amd64 platform')"
  wget -q https://go.dev/dl/go1.18.3.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.18.3.linux-amd64.tar.gz
    # go install github.com/tomnomnom/assetfinder@latest
  wget -q https://github.com/tomnomnom/assetfinder/releases/download/v0.1.1/assetfinder-linux-amd64-0.1.1.tgz &&
    tar -xf assetfinder-linux-amd64-0.1.1.tgz && mv assetfinder /usr/bin/assetfinder &> nooutput
else
  echo "(DEBUG) Can't determine version of go for the platform')"
  echo "$CMD"
fi

ln -s /usr/local/go/bin/go /usr/bin/go &> nooutput

wget -q https://github.com/projectdiscovery/subfinder/releases/download/v2.5.2/subfinder_2.5.2_linux_amd64.zip &&
  unzip subfinder_2.5.2_linux_amd64.zip && mv subfinder /usr/bin/subfinder &> nooutput

wget -q https://github.com/projectdiscovery/httpx/releases/download/v1.2.1/httpx_1.2.1_linux_amd64.zip &&
  unzip httpx_1.2.1_linux_amd64.zip && mv httpx /usr/bin/httpx &> nooutput

wget -q wget https://github.com/jaeles-project/gospider/releases/download/v1.1.6/gospider_v1.1.6_linux_x86_64.zip &&
  unzip gospider_v1.1.6_linux_x86_64.zip && mv gospider_v1.1.6_linux_x86_64/gospider /usr/bin/gospider &> nooutput

wget -q https://github.com/lc/gau/releases/download/v2.1.1/gau_2.1.1_linux_386.tar.gz &&
  tar -xf gau_2.1.1_linux_386.tar.gz && mv gau /usr/bin/gau &> nooutput


wget -q https://github.com/lc/subjs/releases/download/v1.0.1/subjs_1.0.1_linux_amd64.tar.gz &&
  tar -xf subjs_1.0.1_linux_amd64.tar.gz && mv subjs  /usr/bin/subjs &> nooutput

# TO-FIX: because of https://github.com/tomnomnom/waybackurls/issues/41
git clone https://github.com/tomnomnom/waybackurls && # go install github.com/tomnomnom/waybackurls@latest
  cd waybackurls && go build main.go  &> nooutput && mv /opt/app/waybackurls/main /usr/bin/waybackurls && cd -

git clone https://github.com/ThreatUnkown/jsubfinder &&
  cd jsubfinder && go build main.go &> nooutput && mv /opt/app/jsubfinder/main /usr/bin/jsubfinder && cd -

#go install github.com/hakluke/hakrawler@latest
git clone https://github.com/hakluke/hakrawler &&
  cd hakrawler && go build &> nooutput  && mv /opt/app/hakrawler/hakrawler /usr/bin/hakrawler && cd -


rm -Rf *.zip *.gz* *.md *.tgz Dockerfile Release nooutput hakrawler jsubfinder waybackurls LICENSE install.sh
