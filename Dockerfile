FROM golang:latest

COPY . /opt/app

WORKDIR /opt/app

RUN bash ./ressources/install.sh

ENTRYPOINT ["bash"]
CMD ["python", "-v"]