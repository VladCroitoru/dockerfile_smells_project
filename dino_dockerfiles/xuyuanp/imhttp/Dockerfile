FROM golang:1.9-alpine

MAINTAINER Xuyuan Pang <xuyuanp@gmail.com>

WORKDIR /go/src/github.com/Xuyuanp/imhttp

ADD . .

RUN go-wrapper install ./...

CMD ["imhttp-remote"]
