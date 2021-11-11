FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

ENV RESTIC_VERSION=0.3.2

RUN apk add --no-cache go git musl-dev openssl ca-certificates && \
    wget https://github.com/restic/restic/releases/download/v${RESTIC_VERSION}/restic-${RESTIC_VERSION}.tar.gz && \
    tar -xzvf restic-${RESTIC_VERSION}.tar.gz && \
    cd restic-${RESTIC_VERSION} && \
    go build build.go && \
    ./build && \
    mv restic /bin/restic && \
    cd ../ && \
    rm -rf restic-* && \
    apk del -q go git musl-dev openssl && \
    rm -rf /var/cache/apk/*
