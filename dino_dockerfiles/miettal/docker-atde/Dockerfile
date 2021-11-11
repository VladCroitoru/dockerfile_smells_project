FROM debian:wheezy

MAINTAINER miettal <taisyo@hongo.wide.ad.jp>

RUN echo "deb http://download.atmark-techno.com/debian/ wheezy main contrib non-free" > /etc/apt/sources.list.d/atmark-techno.list
RUN gpg --keyserver pgp.mit.edu --recv-keys 3874DA771B351757
RUN gpg --armor --export 3874DA771B351757 | apt-key add -
RUN apt-get update

RUN apt-get install -y ca-certificates
RUN apt-get install -y wget
RUN apt-get install -y build-essential
RUN apt-get install -y a420-development-environment

RUN cd /root && wget -q https://armadillo.atmark-techno.com/files/downloads/dist/atmark-dist-20171227.tar.gz
RUN cd /root && wget -q https://armadillo.atmark-techno.com/files/downloads/armadillo-420/source/kernel/linux-3.14-at10.tar.gz
RUN cd /root && tar zxf atmark-dist-20171227.tar.gz
RUN cd /root && tar zxf linux-3.14-at10.tar.gz
RUN cd /root && ln -s atmark-dist-20171227 atmark-dist
RUN cd /root/atmark-dist && ln -s ../linux-3.14-at10 linux-3.x
