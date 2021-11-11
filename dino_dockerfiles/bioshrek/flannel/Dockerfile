# flannel: build
#

FROM google/debian:wheezy
MAINTAINER Huan Wang <shrekwang1@gmail.com>

RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl build-essential ca-certificates git mercurial bzr
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.3.linux-amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1
RUN mkdir /gopath

ENV GOROOT /goroot
ENV GOPATH /gopath
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

RUN mkdir -p /flannel-binaries/
RUN mkdir -p $GOPATH/src/github.com/coreos
WORKDIR /gopath/src/
RUN git clone https://github.com/coreos/flannel.git github.com/coreos/flannel

WORKDIR /gopath/src/github.com/coreos/flannel
RUN go get -v github.com/tools/godep
RUN pwd 
RUN bash -c ./build
RUN cp ./bin/* /flannel-binaries/
VOLUME /flannel-binaries
