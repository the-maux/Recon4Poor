FROM ubuntu

COPY . /opt/app

WORKDIR /opt/app

# TODO: in the install.sh
ENV PATH="/usr/local/go/bin:${PATH}"
# TODO: in the install.sh
ENV PYTHONPATH="/opt/app"

RUN bash ./ressources/install.sh

CMD ["python3", "./src/main.py"]
