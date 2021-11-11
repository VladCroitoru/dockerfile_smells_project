FROM ubuntu:14.04
MAINTAINER Malasits Geza version: 0.3 

RUN apt-get update
RUN apt-get -y install  git automake build-essential  libcurl4-openssl-dev libncurses5-dev pkg-config automake yasm

RUN cd /opt ; git clone https://github.com/tpruvot/cpuminer-multi
RUN cd /opt/cpuminer-multi ; ./build.sh
RUN cd /opt/cpuminer-multi ; make install
