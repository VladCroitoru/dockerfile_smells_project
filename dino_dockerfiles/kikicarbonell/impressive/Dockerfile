FROM ubuntu:16.04

MAINTAINER Enrique Carbonell <kikicarbonell[at]gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update  && \
    apt-get install -y impressive && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /slides

ENTRYPOINT ["/usr/bin/impressive"]



