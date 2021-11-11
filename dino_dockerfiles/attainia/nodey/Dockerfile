FROM node:9.11.1-alpine
MAINTAINER Attainia Development <developers@attainia.com>
LABEL name="Nodey"
LABEL description="A light, basic Node Alpine image with the NPM CI capability"

ENV BUILD_PACKAGES bash build-base git

RUN apk update && \
    apk upgrade && \
    apk add $BUILD_PACKAGES && \
    rm -rf /var/cache/apk/*

RUN npm i -g npm@5.8.0
