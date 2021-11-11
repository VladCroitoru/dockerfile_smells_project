FROM node:12.18.2-alpine

MAINTAINER togglecorp info@togglecorp.com

RUN apk update\
    && apk add --no-cache gawk git rsync bash findutils

WORKDIR /code

COPY ./package.json ./yarn.lock /code/
RUN yarn install --network-concurrency 1

COPY . /code/
