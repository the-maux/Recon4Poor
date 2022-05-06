FROM golang:latest

COPY . /opt/app

WORKDIR /opt/app

RUN bash ./ressources/install.sh

RUN apt -y install python3 python3-pip

ENTRYPOINT ["bash"]
CMD ["python", "-v"]