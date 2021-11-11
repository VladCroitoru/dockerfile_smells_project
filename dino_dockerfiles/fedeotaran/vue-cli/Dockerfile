FROM node:slim

MAINTAINER Fede Otaran <fedeotaran@gmail.com>

RUN npm install --quiet --global vue-cli

RUN mkdir /code
COPY . /code

WORKDIR /code
