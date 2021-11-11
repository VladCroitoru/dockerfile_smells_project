FROM ubuntu:14.04

MAINTAINER ZOL <hello@zol.fr>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /src

RUN apt-get update && apt-get install -y \
    nodejs \
    npm

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN npm install -g bower
RUN npm install -g gulp
