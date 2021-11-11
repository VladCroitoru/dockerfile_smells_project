FROM ubuntu:trusty
MAINTAINER maglovato

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y telnet
RUN apt-get install -y curl
RUN apt-get install -y openssh-client
RUN apt-get install -y unzip
RUN apt-get install -y make
RUN apt-get install -y gcc
RUN curl https://www.python.org/ftp/python/2.6.6/Python-2.6.6.tgz -o /tmp/p266.tgz
RUN cd /tmp && tar zxvf p266.tgz
RUN cd /tmp/Python-2.6.6 && ./configure
RUN cd /tmp/Python-2.6.6 && make
RUN cd /tmp/Python-2.6.6 && make install
