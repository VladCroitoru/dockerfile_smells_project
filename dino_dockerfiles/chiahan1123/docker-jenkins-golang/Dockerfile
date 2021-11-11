FROM golang:1.8-alpine
LABEL maintainer="Eric Chang <chiahan1123@gmail.com>"

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh && \
    rm -rf /var/cache/apk/*

RUN go get -u -v github.com/axw/gocov/gocov && \
    go get -u -v github.com/t-yuki/gocov-xml && \
    go get -u -v gopkg.in/matm/v1/gocov-html && \
    rm -rf $GOPATH/src/*  # since only need the binary
