FROM ubuntu

COPY . /opt/app

WORKDIR /opt/app

RUN bash ./install.sh

ENV PYTHONPATH="/opt/app"

#CMD ["python3", "./src/main.py"]
CMD ["python3", "./src/unit_test.py"]
