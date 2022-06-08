#!/usr/bin/env bash

apt -yqq update &> nooutput
apt -yqq install python3 python3-pip wget git unzip nano
apt-get clean &> nooutput

## install python ressources
#git clone https://github.com/dark-warlord14/LinkFinder.git
#git clone https://github.com/nsonaniya2010/SubDomainizer.git
#git clone https://github.com/aboul3la/Sublist3r.git
git clone https://github.com/duty1g/subcat

cat ./subcat/requirements.txt > requirement_all.txt
#cat ./LinkFinder/requirements.txt >> requirement_all.txt
#cat ./Sublist3r/requirements.txt >> requirement_all.txt
#cat ./SubDomainizer/requirements.txt | grep -v "requests" | grep -v "argparse" >> requirement_all.txt
#echo "colorama" >> requirement_all.txt
#cat requirement_all.txt | sort -u > requirements.txt
#cat requirements.txt
pip3 install -r requirements_all.txt
#cd /opt/app/LinkFinder && python3 ./setup.py install



#wget -q https://go.dev/dl/go1.18.3.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.18.3.linux-amd64.tar.gz
#
## TO-FIX: because of https://github.com/tomnomnom/waybackurls/issues/41
#git clone https://github.com/tomnomnom/waybackurls.git && # go install github.com/tomnomnom/waybackurls@latest
#  cd waybackurls && go build main.go && ln -s /opt/app/waybackurls/main /usr/bin/waybackurls &> nooutput
#
## go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
#wget -q https://github.com/projectdiscovery/subfinder/releases/download/v2.5.2/subfinder_2.5.2_linux_amd64.zip &&
#  unzip subfinder_2.5.2_linux_amd64.zip && mv ./subfinder /usr/bin/subfinder
#
## go install -v github.com/lc/gau/v2/cmd/gau@latest
#wget -q https://github.com/lc/gau/releases/download/v2.1.1/gau_2.1.1_linux_386.tar.gz &&
#  tar -xvf gau_2.1.1_linux_386.tar.gz && mv ./gau /usr/bin/gau
#
## go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
#wget -q https://github.com/projectdiscovery/httpx/releases/download/v1.2.1/httpx_1.2.1_linux_amd64.zip &&
#  unzip httpx_1.2.1_linux_amd64.zip && mv ./httpx /usr/bin/httpx


export HOME=/opt/app/
export GOPATH=$HOME/go/bin
export PATH=$PATH:$GOPATH
export OUTPUT_DIR=/opt/app

rm -vf go1.18.3.linux-amd64.tar.gz gau_2.1.1_linux_386.tar.gz Dockerfile Release nooutput


#go install github.com/tomnomnom/assetfinder@latest
#go install github.com/hakluke/hakrawler@latest
#go install github.com/jaeles-project/gospider@latest
#go install github.com/dwisiswant0/unew@latest
## GO111MODULE=on go get -u github.com/shenwei356/rush /!\ No need, because: 1 target only by contener
#go install github.com/hiddengearz/jsubfinder@latest
#wget https://raw.githubusercontent.com/hiddengearz/jsubfinder/master/.jsf_signatures.yaml && mv .jsf_signatures.yaml ~/.jsf_signatures.yaml
#go install github.com/projectdiscovery/chaos-client/cmd/chaos@latest
#
#go install github.com/lc/subjs@latest


#cat ./SecretFinder/requirements.txt | grep -v "requests" >> requirement_all.txt
#git clone https://github.com/m4ll0k/SecretFinder.git
