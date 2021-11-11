FROM alpine:3.7

ENV NGHTTP2_VERSION 1.31.0
ENV ARGS=

RUN set -ex && \
    apk add --no-cache --virtual .build-deps \
        openssl-dev \
        gcc \
        g++ \
        make \
        binutils \
        autoconf \
        automake \
        libtool \
        libxml2-dev \
        libev-dev \
        libevent-dev \
        c-ares-dev \
        zlib-dev \
        jemalloc-dev \
        wget && \
    apk add --no-cache --virtual .run-deps \
        libev  \
        openssl \
        zlib \
        c-ares \
        jemalloc && \
    cd /tmp && \
    wget https://github.com/nghttp2/nghttp2/releases/download/v1.31.0/nghttp2-${NGHTTP2_VERSION}.tar.bz2 && \
    tar xf nghttp2-${NGHTTP2_VERSION}.tar.bz2 && \
    cd nghttp2-${NGHTTP2_VERSION} && \
    ./configure --enable-app \
                --without-libxml2 \
                --disable-python-bindings \
                --without-spdylay \
                --without-jemallo &&\
    make install && \
    apk del .build-deps && \
    rm -rf /tmp/* 

CMD exec nghttpx $ARGS


