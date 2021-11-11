FROM ubuntu:latest

MAINTAINER jono wells <_@oj.io>

ENV DEBIAN_FRONTEND=noninteractive

RUN set -eux &&\
  apt-get -y install software-properties-common &&\
  add-apt-repository ppa:mc3man/trusty-media &&\
  apt-get update &&\
  apt-get -y dist-upgrade &&\
  apt-get -y install mencoder &&\
  apt-get clean

CMD [ "mencoder" ]
