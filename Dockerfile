FROM golang:latest

COPY ./install.sh .
COPY . /opt/JSFScan.sh

RUN bash ./install.sh

WORKDIR /opt/JSFScan.sh

CMD ["/bin/bash", "./recon.sh"]
