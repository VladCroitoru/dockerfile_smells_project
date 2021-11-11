FROM alpine:3.7

ARG TZ='Asia/Shanghai'

ENV TZ $TZ
ENV SS_LIBEV_VERSION 3.2.0
ENV KCP_VERSION 20180316 

RUN apk upgrade --update \
    && apk add bash tzdata libsodium \
    && apk add --virtual .build-deps \
        autoconf \
        automake \
        asciidoc \
        xmlto \
        build-base \
        curl \
        libev-dev \
        libtool \
        c-ares-dev \
        linux-headers \
        udns-dev \
        libsodium-dev \
        mbedtls-dev \
        pcre-dev \
        udns-dev \
        tar \
        git \
    && curl -sSLO https://github.com/shadowsocks/shadowsocks-libev/releases/download/v$SS_LIBEV_VERSION/shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \
    && tar -zxf shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \
    && (cd shadowsocks-libev-$SS_LIBEV_VERSION \
    && ./configure --prefix=/usr --disable-documentation \
    && make install ) \
    && curl -sSLO https://github.com/xtaci/kcptun/releases/download/v$KCP_VERSION/kcptun-linux-amd64-$KCP_VERSION.tar.gz \
    && tar -zxf kcptun-linux-amd64-$KCP_VERSION.tar.gz \
    && mv server_linux_amd64 /usr/bin/kcpserver \
    && mv client_linux_amd64 /usr/bin/kcpclient \
    && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && runDeps="$( \
        scanelf --needed --nobanner /usr/bin/ss-* \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | xargs -r apk info --installed \
            | sort -u \
        )" \
    && apk add --no-cache --virtual .run-deps $runDeps \
    && apk del .build-deps \
    && rm -rf kcptun-linux-amd64-$KCP_VERSION.tar.gz \
        shadowsocks-libev-$SS_LIBEV_VERSION.tar.gz \
        shadowsocks-libev-$SS_LIBEV_VERSION \
        /var/cache/apk/*

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
