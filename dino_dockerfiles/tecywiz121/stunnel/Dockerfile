FROM alpine:3.6
LABEL maintainer="Sam Wilson <tecywiz121@hotmail.com>"

ARG STUNNEL_URL=https://www.stunnel.org/downloads/stunnel-5.42.tar.gz
ARG STUNNEL_SHA256=1b6a7aea5ca223990bc8bd621fb0846baa4278e1b3e00ff6eee279cb8e540fab

RUN set -xe \
    && apk update \
    && apk add openssl curl alpine-sdk openssl-dev \
    && mkdir build \
        && cd build \
        && curl -sSL "$STUNNEL_URL" -o stunnel.tar.gz \
        && echo "$STUNNEL_SHA256  stunnel.tar.gz" | sha256sum -c - \
        && tar -xf stunnel.tar.gz --strip 1 \
        && ./configure \
        && make install \
        && cd .. \
        && rm -rf build stunnel.tar.gz \
    && apk --purge del curl alpine-sdk openssl-dev \
    && rm -rf /var/cache/apk/* \
    && mkdir -p /etc/stunnel/

VOLUME ["/etc/stunnel"]

WORKDIR /tmp
CMD ["stunnel", "/etc/stunnel/stunnel.conf"]
