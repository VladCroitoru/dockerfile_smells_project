FROM debian:jessie

LABEL debian.version="8.8" ontologizer.version="2.1" maintainer="Alice Minotto, @ Earlahm Institute" 

USER root

RUN apt-get -y update && apt-get -yy install apt-transport-https && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61 && \
    echo deb [arch=all] https://dl.bintray.com/ontologizer/deb unstable main >> /etc/apt/sources.list.d/ontologizer.list && \
    apt-get update && apt-get -yy install ontologizer-cli

WORKDIR /data/
