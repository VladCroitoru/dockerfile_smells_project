FROM ubuntu:14.04
MAINTAINER Masahji Stewart <masahji@synctree.com>

RUN     apt-get update
RUN     apt-get install -y nodejs npm

RUN     mkdir -p /usr/local/src
COPY    . /usr/local/src/rtc-switchboard

WORKDIR /usr/local/src/rtc-switchboard
RUN     npm install

EXPOSE  8080
ENV     NODE_PORT 8080

ENTRYPOINT /usr/bin/nodejs server.js
