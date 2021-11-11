FROM golang:1.7-alpine
MAINTAINER My Social Observations <mysocialobservations@gmail.com>

RUN apk add --update --update-cache --no-cache \
    git \
    ca-certificates && \
    go get github.com/tdewolff/minify/cmd/minify && \
    apk del --update --update-cache --no-cache \
    git \
    ca-certificates
