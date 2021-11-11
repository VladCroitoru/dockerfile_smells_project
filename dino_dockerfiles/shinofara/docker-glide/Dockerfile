FROM golang:1.7-alpine
MAINTAINER Yuki Shinohara <shinofara+docker@gmail.com>

RUN apk update && \
    apk add --no-cache --virtual .glide-installdeps curl tar && \
    apk add git

RUN curl -LO https://github.com/Masterminds/glide/releases/download/v0.12.3/glide-v0.12.3-linux-amd64.tar.gz && \
    tar zxfv glide-v0.12.3-linux-amd64.tar.gz && \
    mv linux-amd64/glide /usr/local/bin/ && \
    rm -rf glide-v0.12.3-linux-amd64.tar.gz linux-amd64

RUN apk del .glide-installdeps

WORKDIR /work
ENTRYPOINT ["/usr/local/bin/glide"]
