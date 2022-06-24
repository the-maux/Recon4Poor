FROM golang:1.18.3

ENV APP_PATH=/opt/recoon

WORKDIR $APP_PATH

COPY . .

ENV PYTHONPATH=$APP_PATH
ENV GOPATH=$APP_PATH

RUN apt -yqq update  && apt -yqq install python3 python3-pip wget git unzip nano iputils-ping
RUN apt-get clean && ln -s /usr/bin/python3 /usr/bin/python

## Install Python scripts
RUN git clone https://github.com/nsonaniya2010/SubDomainizer && pip install -r SubDomainizer/requirements.txt
RUN git clone https://github.com/aboul3la/Sublist3r && pip install -r Sublist3r/requirements.txt
RUN git clone https://github.com/duty1g/subcat && pip install -r subcat/requirements.txt
RUN git clone https://github.com/m4ll0k/SecretFinder && pip install -r SecretFinder/requirements.txt
#git clone https://github.com/GerbenJavado/LinkFinder.git && cd ./LinkFinder && python setup.py install && cd -

# Install Go tools
RUN go install github.com/projectdiscovery/httpx/cmd/httpx@latest
RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
RUN go install github.com/lc/gau/v2/cmd/gau@latest
RUN go install github.com/tomnomnom/waybackurls@latest
RUN go install github.com/hakluke/hakrawler@latest
RUN git clone https://github.com/ThreatUnkown/jsubfinder && cd jsubfinder && go build main.go && \
    mv $APP_PATH/jsubfinder/main /usr/bin/jsubfinder

RUN mv bin/* /usr/bin
RUN rm -Rf *.zip *.gz* *.md *.tgz Dockerfile Release LICENSE install.sh bin pkg jsubfinder

CMD ["python", "./src/main.py"]
#CMD ["python", "./src/unit_test.py"]
