FROM ubuntu:14.04

MAINTAINER yakumo

RUN apt-get update
RUN apt-get install -qy curl git make software-properties-common gcc mercurial libpcre3 libpcre3-dev zlib1g zlib1g-dev

# install java
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer
RUN update-java-alternatives -s java-8-oracle
RUN apt-get install oracle-java8-set-default

# install go-lang
RUN add-apt-repository ppa:evarlast/golang1.4
RUN apt-get update
RUN apt-get install -qy golang-go

RUN mkdir -p /usr/local/go/bin
ENV GOPATH /usr/local/go
ENV GOBIN /usr/local/go/bin
ENV PATH $PATH:$GOBIN

# go build settings
ENV CGO_ENABLED 0
ENV GOOS linux

# make etcd
RUN go get github.com/coreos/etcd
RUN go build -v -a -ldflags '-w' --installsuffix=etcd github.com/coreos/etcd

# make skydns
RUN go get github.com/skynetservices/skydns
RUN go build -v -a -ldflags '-w' --installsuffix=sky github.com/skynetservices/skydns

# make docker2aci
RUN go get github.com/appc/docker2aci
RUN go build -v -a -ldflags '-w' --installsuffix=d2a github.com/appc/docker2aci

# nginx
# ./configure --prefix=/opt/nginx --with-cc-opt="-static -static-libgcc" --with-ld-opt="-static" --user=www --group=www
