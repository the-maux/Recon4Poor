FROM ubuntu

COPY . /opt/app

WORKDIR /opt/app

ENV PATH="/usr/local/go/bin:${PATH}"  # TODO: in the install.sh
ENV PYTHONPATH="/opt/app"  # TODO: in the install.sh

RUN bash ./ressources/install.sh

CMD ["python3", "./src/main.py"]
