FROM phusion/baseimage

# Update to latest packages
RUN apt-get update

RUN apt-get install -y curl
RUN apt-get install -y g++
RUN apt-get install -y python
RUN apt-get install -y make

ENV NODE_VERSION 4.4.4

WORKDIR /opt
RUN curl https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz | tar xvz
ENV PATH /opt/node-v$NODE_VERSION-linux-x64/bin:$PATH
