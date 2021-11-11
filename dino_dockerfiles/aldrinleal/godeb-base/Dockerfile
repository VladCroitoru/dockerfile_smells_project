FROM ubuntu:14.04

RUN apt-get update ; apt-get -y install mercurial bzr git curl wget build-essential

RUN curl -sL https://godeb.s3.amazonaws.com/godeb-amd64.tar.gz | tar xzvf - -C /usr/bin ; godeb install 1.3.1

ENV GOPATH /home/ubuntu/go
ENV PATH /usr/local/go/bin:$GOPATH/bin:$PATH

