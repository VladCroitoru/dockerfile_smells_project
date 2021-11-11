FROM golang:1.3

MAINTAINER Ian Blenke <ian@blenke.com>

RUN go get github.com/ianblenke/statsd-librato

EXPOSE 8125

ENTRYPOINT ["/go/bin/statsd-librato"]
