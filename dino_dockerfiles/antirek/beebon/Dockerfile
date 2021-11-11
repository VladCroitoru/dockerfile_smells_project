FROM node:12.16.1

ARG NODE_ENV

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN git clone https://github.com/antirek/beebon /usr/src/app

RUN npm install
