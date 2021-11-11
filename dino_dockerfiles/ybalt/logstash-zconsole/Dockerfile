FROM golang:1.7-alpine

MAINTAINER ybaltouski@gmail.com

RUN apk update && apk add zeromq-dev alpine-sdk

ADD logstash-zconsole.go /go/src/github.com/golang/ybalt/logstash-zconsole/
RUN go get github.com/tools/godep \
    && go get github.com/pebbe/zmq4  \
    && go install github.com/golang/ybalt/logstash-zconsole

ENTRYPOINT /go/bin/logstash-zconsole

EXPOSE 8080