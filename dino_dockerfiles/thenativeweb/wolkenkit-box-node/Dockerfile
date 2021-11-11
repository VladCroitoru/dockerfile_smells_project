FROM node:10.13.0-alpine
MAINTAINER the native web <hello@thenativeweb.io>

ADD ./keys /keys/

RUN apk update && \
    apk upgrade && \
    apk add curl git openssl && \
    curl --output /usr/local/bin/dumb-init -L https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \
    chmod a+x /usr/local/bin/dumb-init
