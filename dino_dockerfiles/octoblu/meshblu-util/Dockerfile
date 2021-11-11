FROM node:0.10.38
MAINTAINER Octoblu <docker@octoblu.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY *.js /usr/src/app/
COPY *.coffee /usr/src/app/
COPY src /usr/src/app/src
RUN npm link
