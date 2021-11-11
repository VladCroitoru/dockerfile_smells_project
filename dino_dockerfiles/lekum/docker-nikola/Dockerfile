FROM ubuntu:xenial
MAINTAINER Alejandro Guirao <lekumberri@gmail.com>
RUN mkdir -p /opt/nikola/src
WORKDIR /opt/nikola/src
ENV UPDATED_AT 2017-02-10-09-35
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev libxml2-dev libxslt1-dev python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
