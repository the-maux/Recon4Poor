#!/usr/bin/env bash

cd /opt/

git clone https://github.com/the-maux/JSFScan.sh.git

# install python3 if not present
apt -y update && apt -y install python3 python3-pip && apt-get clean

cd /opt/JSFScan.sh/tools

# install python resssources
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
cd /opt/JSFScan.sh/tools/LinkFinder && python3 ./setup.py install


kjkjkjh giu iuyiuyiuyiuyi y
# install go resssources
go get github.com/tomnomnom/waybackurls
GO111MODULE=on go get -u github.com/tomnomnom/assetfinder
GO111MODULE=on go get -v github.com/hakluke/hakrawler
GO111MODULE=on go get -u github.com/jaeles-project/gospider
GO111MODULE=on go get -u github.com/dwisiswant0/unew
# GO111MODULE=on go get -u github.com/shenwei356/rush /!\ No need, because: 1 target only by contener
GO111MODULE=on go get -u github.com/hiddengearz/jsubfinder
GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
wget https://raw.githubusercontent.com/hiddengearz/jsubfinder/master/.jsf_signatures.yaml && mv .jsf_signatures.yaml ~/.jsf_signatures.yaml
GO111MODULE=on go get -v github.com/projectdiscovery/chaos-client/cmd/chaos
GO111MODULE=on go get github.com/lc/gau
GO111MODULE=on go get github.com/lc/subjs

cd /opt/JSFScan.sh/

export HOME=/opt/JSFScan/
export GOPATH=$HOME/go/bin
export PATH=$PATH:$GOPATH
export OUTPUT_DIR=/opt/JSFScan





