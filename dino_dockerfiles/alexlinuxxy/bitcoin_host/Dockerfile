FROM ubuntu:16.04
MAINTAINER "nikshuang@163.com"
RUN apt-get update && apt-get install git make g++ autoconf automake pkg-config libtool libdb++-dev bsdmainutils libevent-dev libssl-dev libboost-filesystem-dev libboost-system-dev libboost-thread-dev libboost-chrono-dev libboost-test-dev libboost-program-options-dev git vim -y
COPY 30proxy /etc/apt/apt.conf.d/

WORKDIR /opt
RUN git clone https://github.com/bitcoin/bitcoin.git

EXPOSE 8333
