FROM golang:latest

WORKDIR /opt/app

COPY . /opt/app

RUN bash ./install.sh

CMD ["python", "-v"]
