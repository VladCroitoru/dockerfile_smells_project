FROM ubuntu:14.04
MAINTAINER Nguyen Sy Thanh Son <thanhson1085@gmail.com>

RUN \
    apt-get update && \
    apt-get install -y python3-pip libyaml-dev

WORKDIR /build
ADD . /build
COPY config/config.py.dev /build/config/config.py

RUN pip3 install -r requirements.txt
CMD python3 run.py

EXPOSE 5000
