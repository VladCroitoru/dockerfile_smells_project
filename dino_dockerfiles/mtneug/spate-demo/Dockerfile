FROM golang:1.9-alpine
MAINTAINER Matthias Neugebauer

COPY . /go/src/github.com/mtneug/spate-demo
RUN go install -v github.com/mtneug/spate-demo/cmd/...

EXPOSE 5000
