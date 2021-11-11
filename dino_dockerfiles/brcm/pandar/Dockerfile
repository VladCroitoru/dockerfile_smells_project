FROM alpine:edge
MAINTAINER AliYunECS <support@aliyun.com>

RUN apk update \
    && apk add python libsodium unzip wget curl \
    && rm -rf /var/cache/apk/*

RUN wget --no-check-certificate https://github.com/brcm/pandar/releases/download/1/pandar.zip -O /tmp/pandar.zip \
    && unzip -d /tmp /tmp/pandar.zip \
    && mv /tmp/shadowsocks /shadowsocks \
    && chmod +x /shadowsocks/frpc \
    && rm -rf /tmp/*

ADD c/core /pandar.json
ADD c/port /pandar.port.ini
ADD c/init /pandar.sh

WORKDIR /
EXPOSE 80

CMD sh /pandar.sh
