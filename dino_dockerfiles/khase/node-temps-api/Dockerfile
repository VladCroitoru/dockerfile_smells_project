FROM node:8-alpine
MAINTAINER <Hasenbank.ken@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./package.json /usr/src/app
COPY ./package-lock.json /usr/src/app
COPY ./server.js /usr/src/app

RUN npm install --production

EXPOSE 80

ENTRYPOINT npm run prod