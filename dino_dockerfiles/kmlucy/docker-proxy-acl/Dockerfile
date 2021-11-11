FROM golang:1-alpine3.5
LABEL maintainer "Kyle Lucy <kmlucy@gmail.com>"

COPY files /go/src/app

WORKDIR /go/src/app

ENV OPTIONS="-a containers"

CMD rm -f /tmp/docker-proxy-acl/docker.sock && go run docker-proxy-acl.go $OPTIONS
