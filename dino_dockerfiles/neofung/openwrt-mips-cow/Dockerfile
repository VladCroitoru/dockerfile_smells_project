from phusion/baseimage:0.9.16

maintainer Neo Fung <neosfung@gmail.com>

ENV DEBIAN_FRONTED noninteractive

COPY build.sh build.sh
RUN apt-get update
RUN apt-get install -y --force-yes dialog gcc-4.7 build-essential
RUN apt-get install -y --force-yes golang-go git
RUN bash build.sh
