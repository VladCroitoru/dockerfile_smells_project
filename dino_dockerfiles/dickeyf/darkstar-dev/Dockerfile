FROM ubuntu:14.04

RUN sudo dpkg --add-architecture i386
RUN apt-get update && apt-get -fy install software-properties-common && add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt-get update && apt-get -fy install automake cpp:i386 g++:i386 gawk gcc:i386 g++-4.9:i386 gcc-4.9:i386 liblua5.1-0-dev liblua5.1-0-dev:i386 libmysqlclient-dev:i386 libtool:i386 git make libzmq3-dev:i386 libzmq3-dev
RUN cd /usr/lib/i386-linux-gnu/ && ln -s liblua5.1.so liblua.so
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 90

WORKDIR ~/

RUN mkdir /source

VOLUME ["/source"]

