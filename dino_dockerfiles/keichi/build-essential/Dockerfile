FROM ubuntu:trusty

MAINTAINER Keichi Takahashi <keichi.t@me.com>

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update && \
    apt-get install -y git m4 build-essential gfortran wget && \
    wget -O - http://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.gz | tar xzvf - && \
    wget -O - http://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz | tar xzvf - && \
    wget -O - http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz | tar xzvf - && \
    cd autoconf* && ./configure && make && make install && cd .. && \
    cd automake* && ./configure && make && make install && cd .. && \
    cd libtool* && ./configure && make && make install && cd .. && \
    rm -rf autoconf* automake* libtool*

