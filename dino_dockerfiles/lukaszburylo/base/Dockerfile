FROM ubuntu:latest
MAINTAINER Lukasz Burylo <lukasz@burylo.com>

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

ENV LC_ALL C.UTF-8
ENV TERM xterm

RUN apt-get -qq update &&\
    apt-get dist-upgrade -y --no-install-recommends

RUN apt-get clean &&\
    apt-get autoremove &&\
    rm -rf /build &&\
    rm -rf /tmp/* /var/tmp/* &&\
    rm -rf /var/lib/apt/lists/*
