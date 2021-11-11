FROM alpine:3.4
MAINTAINER Luis Alonzo <wichon@gmail.com>

RUN apk upgrade --update \
    && apk add alpine-sdk libevent-dev libevent git bsd-compat-headers \
    && git clone --depth 1 git://github.com/nicolasff/webdis.git /tmp/webdis \
    && cd /tmp/webdis/ \
    && make clean all \
    && mkdir /webdis \
    && cp webdis webdis.json /webdis \
    && apk del --purge alpine-sdk libevent-dev bsd-compat-headers git \
    && rm -rf /tmp/webdis \
    && rm -f /var/cache/apk/*

EXPOSE 7379
