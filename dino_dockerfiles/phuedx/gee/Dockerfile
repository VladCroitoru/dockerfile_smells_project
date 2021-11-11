FROM ubuntu:16.04

MAINTAINER Sam Smith <yo@samsmith.io>

RUN apt-get update &&\
  apt-get install --yes iproute2 iptables

RUN mkdir -p /opt/gee/bin
COPY gee /opt/gee/bin

CMD /opt/gee/bin/gee; /bin/bash
