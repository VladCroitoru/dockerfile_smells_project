FROM ubuntu:14.04
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
MAINTAINER developerworks <developerworks@163.com>
RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y wget
RUN apt-get install -y python
RUN wget http://nodejs.org/dist/v0.10.31/node-v0.10.31.tar.gz
RUN tar zxf node-v0.10.31.tar.gz && cd node-v0.10.31 && ./configure && make && make install