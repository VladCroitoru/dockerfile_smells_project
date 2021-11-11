FROM node:8-alpine

RUN apk add --no-cache make gcc g++ python

RUN addgroup -S nodejs && adduser -S -g nodejs nodejs
USER nodejs

ENV NODE_ENV=production
ENV APP_DIR=/home/nodejs/app
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR
COPY package.json $APP_DIR
COPY package-lock.json $APP_DIR
RUN npm i --quiet
COPY . $APP_DIR

USER root
RUN npm cache clean --force
RUN apk del make gcc g++ python
USER nodejs

ENTRYPOINT node server.js
