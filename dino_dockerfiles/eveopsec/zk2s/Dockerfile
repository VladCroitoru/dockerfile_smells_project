FROM golang:1.7-alpine

RUN apk add --no-cache git

RUN go get github.com/eveopsec/zk2s

RUN mkdir /zk2s

WORKDIR /zk2s

ENTRYPOINT /go/bin/zk2s start
