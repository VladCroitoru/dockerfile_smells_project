FROM golang:1.6
MAINTAINER Hugo González Labrador

RUN mkdir -p /var/log/clawio
RUN mkdir -p /etc/clawio/

ADD . /go/src/github.com/clawio/authentication
WORKDIR /go/src/github.com/clawio/authentication
RUN go get ./...
WORKDIR /go/src/github.com/clawio/authentication/server
RUN go install

RUN cp /go/src/github.com/clawio/authentication/config.json /etc/clawio/authentication.conf

ENTRYPOINT server -config /etc/clawio/authentication.conf
