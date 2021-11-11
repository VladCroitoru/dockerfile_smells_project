FROM crowdriff/baseimage:latest

MAINTAINER Abhinav Ajgaonkar <abhi@crowdriff.com>

ENV	GOROOT /goroot
ENV GOPATH	/gopath
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

RUN \
	apt-get update; \
	apt-get install -y -qq git make; \
	mkdir -p /goroot /gopath; \
	wget -O - https://storage.googleapis.com/golang/go1.4.linux-amd64.tar.gz | tar xzf - --strip-components=1 -C "/goroot"; \
	go get github.com/tools/godep