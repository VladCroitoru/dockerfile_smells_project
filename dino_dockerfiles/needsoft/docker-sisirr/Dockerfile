FROM alpine:3.7

LABEL maintainer="noone"

ARG TZ='Asia/Shanghai'
ARG BRANCH=akkariiin/dev
ARG DIR_NAME=akkariiin-dev

ENV TZ $TZ
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

WORKDIR shadowsocks
COPY user-config.json ./config.json

ENTRYPOINT [ "python", "server.py"]
