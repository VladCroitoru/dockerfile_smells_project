FROM ubuntu:latest

MAINTAINER rudijs <ooly.me@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

RUN apt-get update

RUN apt-get upgrade -y

RUN         apt-get -y install redis-server

ENTRYPOINT  ["/usr/bin/redis-server"]