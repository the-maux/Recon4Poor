FROM ubuntu

COPY . /opt/app

WORKDIR /opt/app

RUN bash ./ressources/install.sh

ENV PYTHONPATH="/opt/app"

CMD ["python3", "./src/main.py"]
