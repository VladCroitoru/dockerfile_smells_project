FROM golang:1.7.4

MAINTAINER labs.garsue@gmail.com

ENV BACKLOG_DOMAIN backlog.jp

RUN go get github.com/garsue/bnotify/cmd/bnotify

ENTRYPOINT ["bnotify"]
