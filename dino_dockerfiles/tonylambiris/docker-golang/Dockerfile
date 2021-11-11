FROM alpine:3.7

MAINTAINER Dustin Willis Webber

ENV OS=linux ARCH=amd64 GO_VERSION=1.11.2 GOROOT=/usr/local/go GOPATH=/go
ENV PATH="$GOPATH/bin:$GOROOT/bin:$PATH"

RUN apk add --no-cache autoconf automake bash curl gcc g++ git make rpm \
	ncurses tar xz upx python2 ruby ruby-dev cairo-dev nodejs nodejs-npm \
	libc-dev libc6-compat libffi-dev libpng-dev && \
	mkdir -p /go && chmod 775 /go && \
	curl -sSL https://golang.org/dl/go$GO_VERSION.$OS-$ARCH.tar.gz | \
		tar -C /usr/local -xz && strip /usr/local/go/bin/* && \
	go get -v github.com/tonylambiris/pkgcloud/cmd/... && \
	gem install --no-ri --no-rdoc fpm thor-scmversion

WORKDIR /source
