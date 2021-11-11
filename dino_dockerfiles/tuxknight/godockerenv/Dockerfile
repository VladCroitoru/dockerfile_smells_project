FROM golang:1.6
MAINTAINER Grissom

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

RUN go get github.com/labstack/echo && \
    go get github.com/go-sql-driver/mysql && \
    go get gopkg.in/yaml.v2 && \
    go get github.com/chanxuehong/wechat/corp && \
    go get github.com/bitly/go-simplejson && \
    go get github.com/alecthomas/log4go && \
    go get github.com/dgrijalva/jwt-go && \
    go get github.com/valyala/fasthttp
