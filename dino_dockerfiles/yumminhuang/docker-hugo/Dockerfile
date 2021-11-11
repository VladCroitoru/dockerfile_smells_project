FROM alpine:latest

LABEL maintainer="Yaming Huang<yumminhuang@gmail.com>"

ARG HUGO_VERSION=0.62.0

RUN apk add --no-cache --update curl ca-certificates && \
    cd /tmp/ && \
    curl -sSL https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz | tar xz && \
    mv hugo* /usr/bin/hugo && \
    apk del curl ca-certificates && \
    rm /var/cache/apk/*

VOLUME ["/website", "/public"]

EXPOSE 1313

WORKDIR /website

ENTRYPOINT ["/usr/bin/hugo"]
