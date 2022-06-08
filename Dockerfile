FROM ubuntu

COPY . /opt/app

WORKDIR /opt/app

ENV PYTHONPATH="/opt/app"

RUN bash ./ressources/install.sh

CMD ["python3", "./src/main.py"]
