FROM alpine:3.7

LABEL maintainer="none"

ARG TZ='Asia/Shanghai'
ARG BRANCH=akkariiin/dev
ARG DIR_NAME=akkariiin-dev
ARG KCP_VERSION=20180316

ENV TZ $TZ
ENV KCP_DOWNLOAD_URL https://github.com/xtaci/kcptun/releases/download/v$KCP_VERSION/kcptun-linux-amd64-$KCP_VERSION.tar.gz
ENV SSRR_DOWNLOAD_URL https://github.com/shadowsocksrr/shadowsocksr/archive/$BRANCH.tar.gz

RUN if [ $(wget -qO- ipinfo.io/country) == CN ]; then echo "http://mirrors.ustc.edu.cn/alpine/v3.7/main/" > /etc/apk/repositories ;fi \
    && apk update --no-cache upgrade \
    && apk --no-cache add libsodium python tzdata \
    && wget -qO- --no-check-certificate ${SSRR_DOWNLOAD_URL} | tar -xzf - -C . \
    && cp -R shadowsocksr-$DIR_NAME/shadowsocks . \
    && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && rm -rf shadowsocksr-$DIR_NAME \
              /var/cache/apk/*

RUN apk upgrade --update \
    && apk add bash tzdata libsodium \
    && apk add --virtual \
        autoconf \
        automake \
        xmlto \
        build-base \
        curl \
        c-ares-dev \
        libev-dev \
        libtool \
        linux-headers \
        udns-dev \
        libsodium-dev \
        mbedtls-dev \
        pcre-dev \
        udns-dev \
        tar \
        git

RUN wget --no-check-certificate  ${KCP_DOWNLOAD_URL} \
    && tar -zxf kcptun-linux-amd64-$KCP_VERSION.tar.gz \
    && mv server_linux_amd64 /usr/bin/kcpserver \
    && mv client_linux_amd64 /usr/bin/kcpclient \
    && rm -rf kcptun-linux-amd64-$KCP_VERSION.tar.gz \
        /var/cache/apk/*

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
