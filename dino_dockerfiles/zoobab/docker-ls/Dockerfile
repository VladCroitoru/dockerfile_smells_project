FROM golang:1.8
MAINTAINER Benjamin Henrion <zoobab@gmail.com>

RUN apt-get update
RUN apt-get install -yy jq

ADD . /go/src/github.com/mayflower/docker-ls
WORKDIR /go/src/github.com/mayflower/docker-ls

RUN make clean && make install && cp /go/src/github.com/mayflower/docker-ls/build/bin/* /usr/local/bin/
RUN cp -v scripts/registry* /usr/local/bin/
