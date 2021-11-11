FROM resin/raspberry-pi-python:3.4.8-slim-20180427
MAINTAINER Allan Tribe <atribe13@gmail.com>

ADD . /src
WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "/src/InfluxdbSpeedtest.py"]
