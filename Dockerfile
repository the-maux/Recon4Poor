FROM ubuntu

COPY . /opt/app

WORKDIR /opt/app

ENV PYTHONPATH=$PWD

RUN bash ./ressources/install.sh

CMD ["python3", "./src/main.py"]
