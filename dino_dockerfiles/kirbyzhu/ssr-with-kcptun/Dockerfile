FROM alpine:3.6

ENV KCP_VERSION 20170329
ENV KCP_CONFIG "-t 127.0.0.1:8388 -l :8300 -mode fast2"
ENV KCP_FLAG "true"

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN apk upgrade --no-cache \
    && apk add --no-cache bash tzdata libsodium \
    && apk add --no-cache --virtual .build-deps \
        autoconf \
        build-base \
        curl git\
        libev-dev \
        libtool \
        linux-headers \
        udns-dev \
        libsodium-dev \
        mbedtls-dev \
        pcre-dev \
        tar \
        zlib-dev \
        libressl-dev

RUN git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git ssr

RUN curl -sSLO https://github.com/xtaci/kcptun/releases/download/v$KCP_VERSION/kcptun-linux-amd64-$KCP_VERSION.tar.gz \
    && tar -zxf kcptun-linux-amd64-$KCP_VERSION.tar.gz \
    && mv server_linux_amd64 /usr/bin/kcptun

RUN apk add --no-cache --virtual .run-deps $runDeps \
    && apk del .build-deps \
    && rm -rf client_linux_amd64 \
        kcptun-linux-amd64-$KCP_VERSION.tar.gz \
        /var/cache/apk/*

ADD entrypoint.sh /entrypoint.sh

RUN chmod -R 755 /entrypoint.sh

EXPOSE 8388 8300

ENTRYPOINT ["/entrypoint.sh"]
