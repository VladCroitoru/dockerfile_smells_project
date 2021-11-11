FROM alpine:edge
MAINTAINER lyndon li <snakeliwei@gmail.com>

RUN set -ex \
    \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        linux-headers \
        make \
        musl-dev \
        tar \
        git \
        zlib-dev \
        openssl-dev \
        asciidoc \
        xmlto \
        libtool \
        pcre-dev \
    \
    && mkdir -p /src/ss \
    && git clone https://github.com/shadowsocks/shadowsocks-libev.git /src/ss \
    && cd /src/ss \
    && ./configure && make \
    && make install \
    && rm -rf /src \
    && apk del .build-deps

ENTRYPOINT ["ss-server"]
