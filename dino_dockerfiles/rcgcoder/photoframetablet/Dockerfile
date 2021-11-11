FROM node:latest

MAINTAINER RCGCoder <ricardo.cantabran@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update 
#RUN apt-get upgrade -y
RUN apt-get install curl wget android-tools-adb android-tools-fastboot mc -y

WORKDIR /tmp
RUN wget http://security.ubuntu.com/ubuntu/pool/universe/k/kodi/kodi-eventclients-common_15.2+dfsg1-3ubuntu1_all.deb
RUN wget http://security.ubuntu.com/ubuntu/pool/universe/k/kodi/kodi-eventclients-kodi-send_15.2+dfsg1-3ubuntu1_all.deb 
RUN dpkg -i *.deb

RUN rm *.deb

RUN mkdir -p /usr/src/app 
RUN mkdir -p /usr/src/app/src
RUN mkdir -p /usr/src/app/src/tplink
RUN mkdir -p /usr/src/app/src/config

WORKDIR /usr/src/app
RUN wget https://raw.githubusercontent.com/RCGCoder/tplink-hs100/master/tplink-hub/package.json
RUN wget https://raw.githubusercontent.com/RCGCoder/tplink-hs100/master/tplink-hub/index.js
RUN npm install
RUN npm install exec-async

WORKDIR /usr/src/app/src/tplink
RUN wget https://raw.githubusercontent.com/RCGCoder/tplink-hs100/master/tplink-hub/src/tplink/index.js

WORKDIR /usr/src/app/src/config
RUN wget https://raw.githubusercontent.com/RCGCoder/tplink-hs100/master/tplink-hub/src/config/logger.js
