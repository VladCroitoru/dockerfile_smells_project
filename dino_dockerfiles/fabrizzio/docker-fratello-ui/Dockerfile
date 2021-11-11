FROM ruby:2.2
MAINTAINER Dieter Provoost <dieter.provoost@marlon.be>

# Use UTF-8 (see https://oncletom.io/2015/docker-encoding/)
ENV LANG C.UTF-8

RUN apt-get update

RUN apt-get install -y npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN apt-get install -y default-jre
RUN gem install sass

RUN npm install -g grunt-cli
RUN npm install -g bower
