FROM ubuntu:16.04

MAINTAINER Adrian Lopez <adrianlzt@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q update &&\
    apt-get -q upgrade -y &&\
    apt-get -q install -y software-properties-common dpkg gdebi-core add-apt-key

RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ xenial universe multiverse" &&\
    add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ xenial-updates universe multiverse"

RUN apt-get -q install -y openjdk-8-jre-headless


RUN add-apt-key -k keyserver.ubuntu.com 320E6224 &&\
    add-apt-repository "deb http://download.eclipse.org/package-drone/release/current/ubuntu package-drone default"

EXPOSE 8080

VOLUME ["/var/lib/package-drone-server/storage"]

CMD ["/usr/lib/package-drone-server/instance/server"]

ENV PACKAGEDRONE_VERSION 0.14.1

RUN apt-get -q update &&\
    apt-get -q install -y org.eclipse.packagedrone.server=${PACKAGEDRONE_VERSION}
