FROM golang:latest

COPY . /opt/app

WORKDIR /opt/app

RUN export PYTHONPATH=$PWD

RUN bash ./ressources/install.sh

CMD ["python3", "./src/main.py"]
