FROM node:8-alpine
MAINTAINER Aaron Scherer <aequasi@gmail.com>

ENV BUILD_PACKAGES="git python gcc make g++"
ENV ESSENTIAL_PACKAGES="zlib libuv curl openssl musl-dev linux-headers curl ca-certificates"

RUN apk add --update --no-cache $ESSENTIAL_PACKAGES $BUILD_PACKAGES \
    && update-ca-certificates \
