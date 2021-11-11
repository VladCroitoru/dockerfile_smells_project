FROM ubuntu:latest

MAINTAINER Henry Mohn <henry@toasterlint.com>

RUN apt-get update -yq && apt-get install -yq fio

RUN mkdir /data /config

ADD *.fio /config/
ADD start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]
