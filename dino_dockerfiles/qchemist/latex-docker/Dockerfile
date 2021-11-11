FROM ubuntu:xenial
MAINTAINER qchemist 
ENV DEBIAN_FRONTEND noninteractive

#RUN echo "Hello World"

RUN apt-get update -q && apt-get install -qy \
    texlive-full \
    gnuplot \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]
