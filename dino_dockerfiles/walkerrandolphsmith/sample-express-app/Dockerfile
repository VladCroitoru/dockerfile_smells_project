FROM node:argon

MAINTAINER Walker Randolph Smith, walkerrandolphsmith@gmail.com

RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY package.json /usr/app
RUN npm install
COPY ./src /usr/app/src
RUN npm run prod:build
RUN npm run prod:start