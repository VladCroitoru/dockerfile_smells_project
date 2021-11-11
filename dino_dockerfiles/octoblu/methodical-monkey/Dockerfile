FROM golang:1.8
MAINTAINER Octoblu, Inc. <docker@octoblu.com>

WORKDIR /go/src/github.com/octoblu/methodical-monkey
COPY . /go/src/github.com/octoblu/methodical-monkey

RUN env CGO_ENABLED=0 go build -o methodical-monkey -a -ldflags '-s' .

CMD ["./methodical-monkey"]
