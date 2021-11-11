FROM ubuntu:14.04
MAINTAINER Yannick Pereira-Reis <yannick.pereira.reis@gmail.com>

ENV HOME /root
ENV NODE_PATH /usr/local/lib/node_modules

RUN apt-get update -qq
RUN apt-get install -y -qq git curl wget

# install npm
RUN apt-get install -y -qq npm
RUN ln -s /usr/bin/nodejs /usr/bin/node

# install bower
RUN npm install -g bower
RUN npm install -g grunt-cli
RUN npm install -g gulp


VOLUME ["/app"]

WORKDIR /app

CMD []

