FROM golang:wheezy 
MAINTAINER Toomore Chiang <toomore0929@gmail.com>

RUN go get github.com/toomore/plivo-go && \
    cd /go/src/github.com/toomore/plivo-go && \
    go get -v ./... && \
    cd /go/src && \
    rm -rf ./* 
