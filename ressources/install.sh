#!/usr/bin/env bash

apt -y update &> nooutput &> nooutput
apt -y install python3 python3-pip wget git &> nooutput
apt-get clean &> nooutput
ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip

## install python ressources
#git clone https://github.com/codingo/Interlace.git
#git clone https://github.com/dark-warlord14/LinkFinder.git
#git clone https://github.com/m4ll0k/SecretFinder.git
#git clone https://github.com/nsonaniya2010/SubDomainizer.git
#git clone https://github.com/aboul3la/Sublist3r.git
## https://github.com/duty1g/subcat # TODO: seems really cool to integrate
#
#cat ./Interlace/requirements.txt > requirement_all.txt
#cat ./SecretFinder/requirements.txt | grep -v "requests" >> requirement_all.txt
#cat ./LinkFinder/requirements.txt >> requirement_all.txt
#cat ./Sublist3r/requirements.txt >> requirement_all.txt
#cat ./SubDomainizer/requirements.txt | grep -v "requests" | grep -v "argparse" >> requirement_all.txt
#echo "colorama" >> requirement_all.txt
#cat requirement_all.txt | sort -u > requirements.txt
#cat requirements.txt
#pip install -r requirements.txt
#cd Interlace && python3 ./setup.py install
#cd /opt/app/LinkFinder && python3 ./setup.py install

wget -q https://go.dev/dl/go1.18.3.linux-amd64.tar.gz &&
    tar -C /usr/local -xzf go1.18.3.linux-amd64.tar.gz &&
    export PATH=$PATH:/usr/local/go/bin
#mkdir -p /usr/local/go/bin && cp ./go/bin/go /usr/local/go/bin/go


# because of https://github.com/tomnomnom/waybackurls/issues/41 we cant go install normaly
# go install github.com/tomnomnom/waybackurls@latest  &> nooutput
git clone https://github.com/tomnomnom/waybackurls.git && cd waybackurls && go build main.go && ln -s /opt/app/waybackurls/main /usr/bin/waybackurls &> nooutput

#go install github.com/tomnomnom/assetfinder@latest
#go install github.com/hakluke/hakrawler@latest
#go install github.com/jaeles-project/gospider@latest
#go install github.com/dwisiswant0/unew@latest
## GO111MODULE=on go get -u github.com/shenwei356/rush /!\ No need, because: 1 target only by contener
#go install github.com/hiddengearz/jsubfinder@latest
#go install github.com/projectdiscovery/httpx/cmd/httpx@latest
#go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
#wget https://raw.githubusercontent.com/hiddengearz/jsubfinder/master/.jsf_signatures.yaml && mv .jsf_signatures.yaml ~/.jsf_signatures.yaml
#go install github.com/projectdiscovery/chaos-client/cmd/chaos@latest
#go install github.com/lc/gau@latest
#go install github.com/lc/subjs@latest

export HOME=/opt/app/
export GOPATH=$HOME/go/bin
export PATH=$PATH:$GOPATH
export OUTPUT_DIR=/opt/app

# rm -f go1.18.3.linux-amd64.tar.gz Dockerfile Release nooutput # TODO: clean !!