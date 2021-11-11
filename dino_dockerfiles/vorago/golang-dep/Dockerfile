FROM golang:alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh && \
    go get -u github.com/golang/dep/...

