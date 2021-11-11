FROM ubuntu:trusty
MAINTAINER Jônatas Renan <jonatas@dcc.ufmg.br>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update
RUN apt-get -qqy install build-essential
RUN apt-get -qqy install libboost-program-options-dev
RUN rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND newt
