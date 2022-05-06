FROM golang:latest

COPY ./resssources/install.sh .

RUN bash ./install.sh

WORKDIR /opt/app
COPY . /opt/app

CMD ["python", "-v"]
