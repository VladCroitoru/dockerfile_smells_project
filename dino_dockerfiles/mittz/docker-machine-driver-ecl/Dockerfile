FROM golang:1.8.0

MAINTAINER Hayahito Kawamitsu

RUN go get github.com/mittz/docker-machine-driver-ecl
RUN go build -o /usr/local/bin/docker-machine-driver-ecl github.com/mittz/docker-machine-driver-ecl/bin/
