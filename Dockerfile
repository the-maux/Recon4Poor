FROM golang:latest

COPY ./install.sh .

RUN bash ./install.sh

WORKDIR /opt/app
COPY . /opt/app

CMD ["python", "-v"]
