# Dart SDK with Sauce Connect

FROM rpadam/dart_docker:latest

MAINTAINER Raphael Adam <raphael.adam@workiva.com, raphael912003@gmail.com>

LABEL Description="This image contains the Dart SDK with Sauce Connect"

RUN apt-get update && apt-get install -y \
    wget \
    && apt-get clean

ENV SC_VERSION 4.3.13

RUN wget -O ./sauce-connect.tar.gz https://saucelabs.com/downloads/sc-$SC_VERSION-linux.tar.gz \
    && tar -zxvf sauce-connect.tar.gz \
    && mv sc-$SC_VERSION-linux/bin/sc /usr/local/bin \
    && rm -rf sauce-connect.tar.gz \
    && rm -rf $SC_VERSION-linux/
