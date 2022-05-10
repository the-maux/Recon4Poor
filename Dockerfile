FROM golang:latest

COPY . /opt/app

WORKDIR /opt/app

ENV PYTHONPATH="/opt/app"

RUN bash ./ressources/install.sh >/dev/null 2>&1

CMD ["python3", "./src/main.py"]
