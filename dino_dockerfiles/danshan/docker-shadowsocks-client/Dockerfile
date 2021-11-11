FROM alpine

MAINTAINER littleqz <littleqz@gmail.com>

RUN echo 'http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories \
    && apk add -U curl libsodium python \
    && curl -sSL https://bootstrap.pypa.io/get-pip.py | python \
    && pip install shadowsocks \
    && apk del curl \
    && rm -rf /var/cache/apk/*

ENV SERVER 0.0.0.0
ENV SERVER_PORT 998
ENV LOCAL_PORT 1080
ENV LOCAL_ADDR 0.0.0.0
ENV PASSWORD default
ENV METHOD aes-256-cfb
ENV TIMEOUT 300

EXPOSE $LOCAL_PORT

CMD sslocal -s "$SERVER" \
            -p "$SERVER_PORT" \
            -l "$LOCAL_PORT" \
            -b "$LOCAL_ADDR" \
            -k "$PASSWORD" \
            -m "$METHOD" \
            -t "$TIMEOUT" \
            -vv
