FROM node:boron
MAINTAINER Shota Sawada

# install Firebase CLI
RUN npm install -g firebase-tools

# install Golang
WORKDIR /root
RUN wget https://storage.googleapis.com/golang/go1.10.2.linux-amd64.tar.gz && \
	tar -C /usr/local -xzf go1.10.2.linux-amd64.tar.gz && \
	rm go1.10.2.linux-amd64.tar.gz

ENV PATH=$PATH:/usr/local/go/bin
ENV GOPATH=/root/go
ENV PATH=$PATH:$GOPATH/bin

RUN go get github.com/gohugoio/hugo
RUN npm install html-minifier -g

WORKDIR /root
