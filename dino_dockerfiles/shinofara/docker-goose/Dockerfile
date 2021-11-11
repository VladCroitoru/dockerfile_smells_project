FROM golang:1.8
MAINTAINER shinofara+docker@gmail.com

RUN go get bitbucket.org/liamstask/goose/cmd/goose

RUN mkdir /db
WORKDIR /

VOLUME ["/db"]

ENTRYPOINT ["/go/bin/goose"]
