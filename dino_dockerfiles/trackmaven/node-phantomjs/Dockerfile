FROM ubuntu:trusty

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -y update

# Basics
RUN apt-get install -y python2.7 python-software-properties
RUN apt-get -y install software-properties-common

# NodeJS
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y nodejs

# PhantomJS
RUN apt-get install -y libfreetype6 libfontconfig
RUN apt-get install -y wget
RUN wget -q https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
RUN tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2
RUN install -t /usr/local/bin phantomjs-1.9.7-linux-x86_64/bin/phantomjs
RUN rm -rf phantomjs-1.9.7-linux-x86_64
RUN rm phantomjs-1.9.7-linux-x86_64.tar.bz2