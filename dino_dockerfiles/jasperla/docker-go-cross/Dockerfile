FROM golang:1.5

MAINTAINER Jasper Lievisse Adriaanse <j@jasper.la>

ENV GOLANG_TARGET_PLATFORM openbsd/amd64

ENV GOLANG_VERSION 1.4.2

ENV GOROOT_BOOTSTRAP /usr/src/go/

ENV APPROOT /go/src/app

RUN curl -sSL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz \
		| tar -v -C /usr/src -xz

RUN curl -o /crosscompile.bash https://raw.githubusercontent.com/davecheney/golang-crosscompile/master/crosscompile.bash

RUN cd $GOROOT_BOOTSTRAP/src \
	&& set -ex \
	&& ./make.bash

RUN mkdir -p $APPROOT
WORKDIR $APPROOT

VOLUME $APPROOT

COPY ./run.sh /
RUN chmod +x /run.sh
CMD ["/run.sh"]
