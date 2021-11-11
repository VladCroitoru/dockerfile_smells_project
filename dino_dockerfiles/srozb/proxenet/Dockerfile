FROM ubuntu:15.10
MAINTAINER Slawomir Rozbicki <docker@rozbicki.eu>

# Prepare deps
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget less vim \
git cmake libpolarssl-dev python-dev python3-dev

WORKDIR /root

ADD . /root/proxenet/
WORKDIR /root/proxenet
RUN cmake . && make -j`grep processor /proc/cpuinfo | wc -l` && make -C keys
RUN mkdir -p proxenet-plugins/autoload

ENTRYPOINT /root/proxenet/proxenet

