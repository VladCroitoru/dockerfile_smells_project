FROM debian:jessie 
MAINTAINER Manuel Pineda <manuel.felipe.pineda@gmail.com>

RUN echo "deb http://ftp.us.debian.org/debian/ testing main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://ftp.us.debian.org/debian/ testing main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update 
RUN apt-get install -y aptitude vim
RUN aptitude install -y wget build-essential python

WORKDIR /home

RUN wget https://nodejs.org/dist/v4.2.0/node-v4.2.0.tar.gz
RUN tar xf node-v4.2.0.tar.gz
WORKDIR /home/node-v4.2.0
RUN ./configure
RUN make 
RUN make install

WORKDIR /home
RUN aptitude install -y libtool pkg-config build-essential autoconf automake uuid-dev
RUN aptitude install -y apt-utils libsodium-dev
RUN wget http://download.zeromq.org/zeromq-4.1.3.tar.gz
RUN tar xf zeromq-4.1.3.tar.gz
WORKDIR /home/zeromq-4.1.3
RUN ./configure
RUN make
RUN make install
RUN ldconfig

WORKDIR /home
RUN rm -rf node-v4.2.0*
RUN rm -rf zeromq-4.1.3*

WORKDIR /
