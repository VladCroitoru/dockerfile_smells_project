# == Whybug
#
# The following volumes may be used with their descriptions next to them:
#
#   /opt/whybug-server/         : Source code of whybug
#
FROM mhart/alpine-node:4
#FROM phusion/baseimage:0.9.18
MAINTAINER Adrian Philipp <info@whybug.com>
EXPOSE 8000/tcp

RUN apk --update add git python make g++

# === General System

# Avoid any interactive prompting
#ENV DEBIAN_FRONTEND noninteractive

# Language specifics
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Install locales
#RUN locale-gen en_US.UTF-8

# Install node dependencies
# The docker cache will be busted when package.json is changed
# http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-dot-js/
RUN mkdir -p /opt/whybug-server
ADD package.json /opt/whybug-server/package.json
RUN cd /opt/whybug-server && npm install

#RUN mkdir -p /opt/whybug-server && \
#    cp -a /tmp/node_modules /opt/whybug-server/

# Load code

# Version using: ADD
#ADD https://github.com/whybug/whybug-server/archive/master.tar.gz /opt/whybug-server/
#RUN cd /opt/whybug-server && \
#    ./bin/install.sh

# Version using: git clone
#RUN git clone https://github.com/whybug/whybug-server.git /opt/whybug-server && \
#    cd /opt/whybug-server && \
#    ./bin/install.sh

# Version using: COPY, see .dockerignore for whitelist
#RUN mkdir /opt/whybug-server
COPY . /opt/whybug-server/
RUN cd /opt/whybug-server && ./bin/install.sh

CMD ["sh", "/opt/whybug-server/bin/start.sh"]

