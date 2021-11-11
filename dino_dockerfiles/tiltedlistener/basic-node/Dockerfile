FROM ubuntu

MAINTAINER tiltedlistener

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y vim

RUN apt-get install -y nodejs
RUN apt-get install -y npm

RUN apt-get install -y git

RUN mkdir /var/www
RUN cd /var/www

RUN git clone https://github.com/tiltedlistener/basic-node.git
