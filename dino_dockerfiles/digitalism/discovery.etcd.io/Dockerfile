FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

# update and cleanup
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get autoremove

# install dependencies
RUN apt-get install -y git-core golang

ADD . /root/discovery.etcd.io
WORKDIR /root/discovery.etcd.io

RUN go run third_party.go install code.google.com/p/rsc/devweb

EXPOSE 8087

CMD GOPATH="${PWD}/third_party" PATH="${PATH}:${PWD}" ./bin/devweb -addr=":8087" github.com/coreos/discovery.etcd.io/dev
