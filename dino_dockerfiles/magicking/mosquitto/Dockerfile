FROM debian:jessie

MAINTAINER Guido Zockoll

ENV DEBIAN_FRONTEND noninteractive

ENV APP_VERSION 1.4.8
RUN apt-get update && apt-get install -qqy wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev uuid-dev libwebsockets-dev pwgen -y
RUN mkdir -p /usr/local/src
WORKDIR /usr/local/src
RUN wget -O mosquitto.tar.gz http://mosquitto.org/files/source/mosquitto-${APP_VERSION}.tar.gz && tar xvzf ./mosquitto.tar.gz
WORKDIR /usr/local/src/mosquitto-${APP_VERSION}
RUN sed -i.bak 's/WITH_WEBSOCKETS:=no/WITH_WEBSOCKETS:=yes/' config.mk && make && make install && /sbin/ldconfig
RUN adduser --system --disabled-password --disabled-login mosquitto
WORKDIR /home/mosquitto
ADD mosquitto.conf /etc/mosquitto/mosquitto.conf
ADD run.sh run.sh

VOLUME /var/mosquitto
RUN chown mosquitto /var/mosquitto

EXPOSE 1883 8080
CMD /home/mosquitto/run.sh
