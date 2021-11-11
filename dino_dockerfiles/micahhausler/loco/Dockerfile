# To build:
# $ docker build -t micahhausler/loco:build .
#
# To run:
# $ docker run micahhausler/loco:build -u user -p password -r <registry> -o - | tee docker.tgz
# or
# $ docker run -v $(pwd):/loco micahhausler/loco:build -u user -p password -r <registry>

FROM golang:1.6-alpine

MAINTAINER Micah Hausler, <hausler.m@gmail.com>

RUN apk -U add git

ADD . /go/src/github.com/micahhausler/loco
WORKDIR /go/src/github.com/micahhausler/loco
RUN go get ./... \
    && go build

ENTRYPOINT ["/go/bin/loco"]
