FROM alpine:latest
MAINTAINER Nobuyuki Matsui <nobuyuki.matsui@gmail.com>

ENV LISTEN_PORT "3000"
ENV GIN_MODE "release"

ENV GOROOT=/usr/lib/go \
    GOPATH=/go \
    PATH=$PATH:$GOROOT/bin:$GOPATH/bin

WORKDIR $GOPATH

RUN apk update && \
    apk add --no-cache --virtual .go musl-dev git go && \
    go get -f -u -v github.com/nmatsui/bearer-auth-api && \
    go install github.com/nmatsui/bearer-auth-api && \
    mv $GOPATH/bin/bearer-auth-api /usr/local/bin && \
    rm -rf $GOPATH && \
    apk del --purge .go

EXPOSE 3000
ENTRYPOINT ["/usr/local/bin/bearer-auth-api"]
