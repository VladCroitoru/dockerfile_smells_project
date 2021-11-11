FROM ubuntu:trusty
MAINTAINER Kaito Udagawa <umiiro.hacker@gmail.com>

# basic setup
RUN apt-get -y update; apt-get -y upgrade; apt-get -y install software-properties-common wget; apt-get -y clean; rm -rf /var/lib/apt/lists/*

# install salt-master
RUN add-apt-repository ppa:saltstack/salt; apt-get -y update; apt-get -y install salt-master; apt-get -y clean; rm -rf /var/lib/apt/lists/*

# image setting
CMD salt-master
EXPOSE 4505 4506
