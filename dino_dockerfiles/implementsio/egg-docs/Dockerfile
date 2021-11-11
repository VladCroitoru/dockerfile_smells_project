# DOC BUILD
FROM node:lts-alpine as builder

ENV EGG_SOURCE=https://github.com/eggjs/egg/archive/master.zip

WORKDIR /usr/src

RUN apk update \
    && apk add ca-certificates \
    && update-ca-certificates \
    && apk add openssl \
    && wget -O /tmp/egg-master.zip "$EGG_SOURCE" \
    && unzip /tmp/egg-master.zip -d ./ \
    && rm /tmp/egg-master.zip \
    && mv egg-master app \
    && cd app \
    && npm i -g npminstall \
    && npminstall \
    && npm run doc-build

# DOC DEPLOY
FROM nginx:stable-alpine

WORKDIR /usr/share/nginx/html

RUN rm *.*

COPY --from=builder /usr/src/app/run/doctools/public/ .
