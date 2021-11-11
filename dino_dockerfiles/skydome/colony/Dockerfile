FROM golang:latest
MAINTAINER Abdulkadir Yaman <abdulkadiryaman@gmail.com>

RUN mkdir /tmp/gopath
ENV GOPATH /tmp/gopath

ENTRYPOINT go get github.com/goskydome/colony && ${GOPATH}/bin/colony
