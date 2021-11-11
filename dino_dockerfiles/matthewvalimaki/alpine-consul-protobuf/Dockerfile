FROM smebberson/alpine-consul-base
MAINTAINER Matthew Valimaki <matthew.valimaki@gmail.com>

ENV PROTOBUF_VERSION=3.0.0-beta-1-bzl-fix

ADD https://github.com/google/protobuf/archive/v"$PROTOBUF_VERSION".tar.gz /tmp/protobuf.tar.gz

RUN \
  apk add --update gcc g++ musl-dev make pkgconfig libtool autoconf automake libuuid file curl && \
  cd /tmp && tar -xzf protobuf.tar.gz && \
  cd protobuf-"$PROTOBUF_VERSION" && ./autogen.sh -s && ./configure && make && make install && \
  apk del gcc g++ musl-dev make pkgconfig libtool autoconf automake libuuid file curl && \
  cd / && rm -rf /tmp/* && rm -rf /var/cache/apk/* /tmp/*
