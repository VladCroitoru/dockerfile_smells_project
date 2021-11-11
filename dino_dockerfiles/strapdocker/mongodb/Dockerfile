FROM phusion/baseimage:latest

ENV MONGO_OPTION false
ENV MONGO_VERSION 2.4.9

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list
RUN apt-get -qq -y update
RUN echo '#!/bin/sh' "\nexit 0" >  /usr/sbin/policy-rc.d
RUN apt-get install -y mongodb-10gen=$MONGO_VERSION

# Create default MongoDB data directory.
RUN mkdir -p /data/db

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017:27017
EXPOSE 28017:28017

RUN mkdir /etc/service/mongod
ADD mongo_start.sh /etc/service/mongod/run
RUN chmod 755 /etc/service/mongod/run

CMD ["/sbin/my_init"]
