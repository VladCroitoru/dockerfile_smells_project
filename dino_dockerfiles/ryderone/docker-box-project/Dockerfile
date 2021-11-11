FROM php:7.4-alpine

RUN apk update \
    && apk upgrade \
    && curl -LSs https://github.com/box-project/box/releases/download/3.11.1/box.phar --output /usr/local/bin/box \
    && chmod 0755 /usr/local/bin/box

ENV BOX_REQUIREMENT_CHECKER=0

WORKDIR /usr/src