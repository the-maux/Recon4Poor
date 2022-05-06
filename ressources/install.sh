#!/usr/bin/env bash

apt -y update && apt -y install python3 python3-pip && apt-get clean

# install python ressources
git clone https://github.com/codingo/Interlace.git
git clone https://github.com/dark-warlord14/LinkFinder.git
git clone https://github.com/m4ll0k/SecretFinder.git
git clone https://github.com/nsonaniya2010/SubDomainizer.git
git clone https://github.com/aboul3la/Sublist3r.git

cat ./Interlace/requirements.txt > requirement_all.txt
cat ./SecretFinder/requirements.txt | grep -v "requests" >> requirement_all.txt
cat ./LinkFinder/requirements.txt >> requirement_all.txt
cat ./Sublist3r/requirements.txt >> requirement_all.txt
cat ./SubDomainizer/requirements.txt | grep -v "requests" | grep -v "argparse" >> requirement_all.txt
echo "colorama" >> requirement_all.txt
cat requirement_all.txt | sort -u > requirements.txt
cat requirements.txt
pip3 install -r requirements.txt
cd Interlace && python3 ./setup.py install
cd /opt/app/LinkFinder && python3 ./setup.py install


# install go ressources
GO111MODULE=on go install github.com/tomnomnom/waybackurls
GO111MODULE=on go install github.com/tomnomnom/assetfinder@latest
GO111MODULE=on go install github.com/hakluke/hakrawler@latest
GO111MODULE=on go install github.com/jaeles-project/gospider@latest
GO111MODULE=on go install github.com/dwisiswant0/unew@latest
# GO111MODULE=on go get -u github.com/shenwei356/rush /!\ No need, because: 1 target only by contener
GO111MODULE=on go install github.com/hiddengearz/jsubfinder@latest
GO111MODULE=on go install github.com/projectdiscovery/httpx/cmd/httpx@latest
GO111MODULE=on go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
wget https://raw.githubusercontent.com/hiddengearz/jsubfinder/master/.jsf_signatures.yaml && mv .jsf_signatures.yaml ~/.jsf_signatures.yaml
GO111MODULE=on go install github.com/projectdiscovery/chaos-client/cmd/chaos@latest
GO111MODULE=on go install github.com/lc/gau@latest
GO111MODULE=on go install github.com/lc/subjs@latest

export HOME=/opt/app/
export GOPATH=$HOME/go/bin
export PATH=$PATH:$GOPATH
export OUTPUT_DIR=/opt/app
