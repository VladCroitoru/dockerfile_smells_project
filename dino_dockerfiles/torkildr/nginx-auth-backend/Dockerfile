FROM node:latest
MAINTAINER torkildr

COPY . /auth-backend
WORKDIR /auth-backend

VOLUME /sessions

RUN npm install

CMD node src/server.js

