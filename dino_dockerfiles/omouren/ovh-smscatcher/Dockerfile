FROM node:alpine

MAINTAINER Olivier Mouren <mouren.olivier@gmail.com>

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN npm install

CMD npm run dev
