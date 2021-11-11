FROM golang:1.9.2-alpine

RUN set -x \
    && apk add --no-cache \
    git \
    build-base \
    tar \
    gzip \
    curl \
    py-pip

RUN set -x \
    && pip install awscli

ENV GOPATH /go
ENV APP_DIR ${GOPATH}/src/github.com

RUN set -x \
    && adduser -D -u 1000 go \
    && echo 'go:password' | chpasswd \
    && mkdir -p ${APP_DIR} \
    && chown -R go:go /go

WORKDIR ${APP_DIR}
USER go

RUN set -x \
    && go get -u github.com/golang/dep/...