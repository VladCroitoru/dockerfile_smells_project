FROM golang

MAINTAINER Qiangning Hong <hongqn@gmail.com>

RUN apt-get update
RUN apt-get install -y npm && ln -s /usr/bin/nodejs /usr/bin/node

RUN go get github.com/tools/godep
