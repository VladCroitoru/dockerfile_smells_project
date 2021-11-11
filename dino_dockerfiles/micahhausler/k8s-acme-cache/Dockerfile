# To build:
# $ docker run --rm -v $(pwd):/go/src/github.com/micahhausler/k8s-acme-cache -w /go/src/github.com/micahhausler/k8s-acme-cache golang:1.7  go build -v -a -tags netgo -installsuffix netgo -ldflags '-w'
# $ docker build -t micahhausler/k8s-acme-cache .
#
# To run:
# $ docker run micahhausler/k8s-acme-cache

FROM golang:1.8-alpine

MAINTAINER Micah Hausler, <hausler.m@gmail.com>

ADD . /go/src/github.com/micahhausler/k8s-acme-cache/

WORKDIR /go/src/github.com/micahhausler/k8s-acme-cache/example

RUN go install .

ENTRYPOINT ["/go/bin/example"]
