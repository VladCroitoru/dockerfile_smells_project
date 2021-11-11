FROM ruby:alpine

RUN apk add --update gcc make musl-dev curl tar binutils rpm git && \
    gem install --no-document fpm && \
    apk del gcc make musl-dev && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/bin/sh", "-c"]
