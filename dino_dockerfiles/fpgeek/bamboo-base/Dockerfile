FROM ubuntu:14.04
MAINTAINER Dave Choi <goodoi09@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV GOPATH /opt/go

RUN apt-get install -yqq software-properties-common && \
    add-apt-repository -y ppa:vbernat/haproxy-1.5 && \
    apt-get update -yqq && \
    apt-get install -yqq haproxy golang git mercurial supervisor && \
    rm -rf /var/lib/apt/lists/*