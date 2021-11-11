FROM gliderlabs/alpine:3.4
MAINTAINER Yann Hodique <yann.hodique@gmail.com>

ENV FUSE_VERSION 2.9.7
RUN apk --update add --virtual build-dependencies --no-cache \
        build-base \
        ca-certificates \
        wget \
        gnupg \
 && update-ca-certificates \
 && rm -rf /var/cache/apk/* \
 && cd / \
 && wget https://github.com/libfuse/libfuse/releases/download/fuse-${FUSE_VERSION}/fuse-${FUSE_VERSION}.tar.gz \
 && wget https://github.com/libfuse/libfuse/releases/download/fuse-${FUSE_VERSION}/fuse-${FUSE_VERSION}.tar.gz.asc \
 && gpg --keyserver hkps.pool.sks-keyservers.net --recv-key 3C4E599F \
 && gpg fuse-${FUSE_VERSION}.tar.gz.asc \
 && tar zxf fuse-${FUSE_VERSION}.tar.gz \
 && cd fuse-${FUSE_VERSION} \
 && ./configure \
 && make -C util LDFLAGS="-all-static -Wl,-v -Wl,--strip-all" V=1 fusermount \
 && cp util/fusermount /usr/local/bin \
 && rm -rf /fuse-* \
 && apk del build-dependencies
