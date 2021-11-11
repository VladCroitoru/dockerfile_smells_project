FROM debian:jessie
MAINTAINER Will Skates <wlskates12@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y git curl wget python-software-properties software-properties-common pkg-config cmake automake libtool libboost-all-dev checkinstall python-setuptools python-pip build-essential g++ tmux

RUN ln -s /usr/bin/libtoolize /usr/bin/libtool

#Libsodium to help with CURVE security for ZeroMQ
RUN mkdir libsodium
RUN cd libsodium
RUN wget https://github.com/jedisct1/libsodium/releases/download/1.0.2/libsodium-1.0.2.tar.gz
RUN tar -xvzf libsodium-1.0.2.tar.gz
RUN cd /libsodium-1.0.2 && ./autogen.sh
RUN cd /libsodium-1.0.2 && ./configure && make check
RUN cd /libsodium-1.0.2 && checkinstall --install --pkgname libsodium --pkgversion 1.0.0 --nodoc
RUN cd /libsodium-1.0.2 && ldconfig

#Install ZeroMQ
RUN wget http://download.zeromq.org/zeromq-4.1.2.tar.gz -P /tmp
RUN tar -zxvf /tmp/zeromq-4.1.2.tar.gz -C /tmp
RUN cd /tmp/zeromq-4.1.2
RUN cd /tmp/zeromq-4.1.2 && ./autogen.sh
RUN cd /tmp/zeromq-4.1.2 && ./configure
RUN cd /tmp/zeromq-4.1.2 && make
RUN cd /tmp/zeromq-4.1.2 && make install
RUN cd /tmp/zeromq-4.1.2 && ldconfig

#Install CZMQ
RUN git clone https://github.com/zeromq/czmq.git /tmp/czmq
RUN cd /tmp/czmq && git checkout v3.0.2
RUN cd /tmp/czmq && ./autogen.sh
RUN cd /tmp/czmq && ./configure && make check
RUN cd /tmp/czmq && make install
RUN cd /tmp/czmq && ldconfig

RUN mkdir /tmp/lib

RUN git clone https://github.com/zeromq/zmqpp.git /tmp/zmqpp
RUN cd /tmp/zmqpp && git checkout tags/4.1.2
RUN cd /tmp/zmqpp && make
#RUN cd /tmp/zmqpp && make check
RUN cd /tmp/zmqpp && make install
#RUN cd /tmp/zmqpp && make installcheck
RUN cd /tmp/zmqpp && ldconfig

RUN git clone https://github.com/zeromq/cppzmq.git /tmp/lib/cppzmq

#May seem weird here but I like to write little test clients with node js so I've included it here.
RUN curl --silent --location https://deb.nodesource.com/setup_0.12 | bash -
RUN apt-get install --yes nodejs

WORKDIR /usr/src