# based on https://raw.githubusercontent.com/smebberson/docker-alpine/master/alpine-confd/Dockerfile
FROM alpine:3.4
MAINTAINER Waleed Samy <waleedsamy634@gmail.com>

ENV CONFD_VERSION=0.11.0

# Statically build confd for Alpine Linux :)
RUN apk add --no-cache go git gcc musl-dev && \
    git clone https://github.com/kelseyhightower/confd.git /src/confd && \
    cd /src/confd && \
    git checkout -q --detach "v$CONFD_VERSION" && \
    cd /src/confd/src/github.com/kelseyhightower/confd && \
    GOPATH=/src/confd/vendor:/src/confd go build -a -installsuffix cgo -ldflags '-extld ld -extldflags -static' -x . && \
    mv ./confd /bin/ && \
    chmod +x /bin/confd && \
    apk del go git gcc musl-dev && \
    rm -rf /src
