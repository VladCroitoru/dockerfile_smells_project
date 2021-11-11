FROM ubuntu:14.04

MAINTAINER TSUYOSHI TORII toritori0318

RUN apt-get -q -y update \
 && apt-get -q -y install git wget curl make

RUN apt-get -q -y clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

#Install fig
RUN curl --insecure -L https://github.com/docker/fig/releases/download/1.0.1/fig-`uname -s`-`uname -m` > /usr/local/bin/fig \
    && chmod +x /usr/local/bin/fig
