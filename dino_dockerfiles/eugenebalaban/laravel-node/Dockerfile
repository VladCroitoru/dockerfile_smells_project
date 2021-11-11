FROM node:12-alpine

RUN apk --update add python make g++ \
  && rm -rf /var/cache/apk/*

WORKDIR /var/www/html