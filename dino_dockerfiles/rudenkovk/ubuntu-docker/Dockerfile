FROM ubuntu:xenial
MAINTAINER "Konstantin Rudenkov" <rudenkovk@gmail.com>

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -yq update && \
    apt-get -yq upgrade && \
    apt-get -yq --no-install-recommends install \
        ca-certificates \
        python-software-properties \
        software-properties-common \
        apt-transport-https \
        aptitude \
        wget \
        curl \
        unzip && \
    add-apt-repository ppa:rudenkovk/nginx+lua && \    
    apt-get autoremove -yq && \
    apt-get clean && \
    apt-get autoclean -yq && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/archive/* /var/lib/apt/lists/*
