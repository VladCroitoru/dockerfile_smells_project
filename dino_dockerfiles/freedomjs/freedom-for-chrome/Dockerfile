# Dockerfile for a standard freedom-for-chrome instance

FROM selenium/node-chrome
MAINTAINER Will Scott <willscott@gmail.com>

USER root

RUN apt-get update -qqy \
  && apt-get -qqy install \
    nodejs nodejs-legacy git npm 

RUN npm install -g grunt-cli
ADD . /freedom-for-chrome
WORKDIR /freedom-for-chrome

RUN npm install

ENV DISPLAY :10

