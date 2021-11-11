FROM alpine:3.4

MAINTAINER Kerri Shotts <kerrishotts@gmail.com>

ENV NODE_VERSION 6.2.0
ENV CORDOVA_VERSION 6.3.0
ENV GULP_VERSION 3.9.1
ENV BABEL_VERSION 5.8.23

RUN apk update && apk --no-cache add \ 
    bash \
    curl \
    git \
    apache-ant \
    nodejs=$NODE_VERSION-r0 \
  && npm install -g --unsafe-perm \
    cordova@$CORDOVA_VERSION \
    gulp@$GULP_VERSION \
    babel@$BABEL_VERSION

VOLUME ["/data"]
WORKDIR /data

EXPOSE 8000