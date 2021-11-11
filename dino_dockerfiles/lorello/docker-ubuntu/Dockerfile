FROM ubuntu:trusty

MAINTAINER LoreLLo <lorenzo.salvadorini@softecspa.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qqy && apt-get install -qqy curl wget git software-properties-common build-essential
RUN apt-add-repository universe
RUN apt-add-repository multiverse

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales
RUN /usr/sbin/update-locale

# Add dockerize binary
# http://jasonwilder.com/blog/2014/10/13/a-simple-way-to-dockerize-applications/
#RUN wget https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-amd64-v0.0.2.tar.gz
#RUN tar -C /usr/local/bin -xvzf dockerize-linux-amd64-v0.0.2.tar.gz

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
