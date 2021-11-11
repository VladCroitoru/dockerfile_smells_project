FROM alpine:latest
MAINTAINER miniers

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

RUN \
  apk --update --upgrade add \
      privoxy haproxy

RUN buildDeps=" \
                asciidoc \
                autoconf \
                build-base \
                curl \
                libtool \
                linux-headers \
                openssl-dev \
                pcre-dev \
                tar \
                xmlto \
        "; \
        set -x \
        && apk add --update openssl \
        && apk add $buildDeps \
        && SS_VERSION=`curl "https://github.com/shadowsocks/shadowsocks-libev/releases/latest" | sed -n 's/^.*tag\/\(.*\)".*/\1/p'` \
        && curl -SL "https://github.com/shadowsocks/shadowsocks-libev/archive/$SS_VERSION.tar.gz" -o ss.tar.gz \
        && mkdir -p /usr/src/ss \
        && tar -xf ss.tar.gz -C /usr/src/ss --strip-components=1 \
        && rm ss.tar.gz \
        && cd /usr/src/ss \
        && ./configure \
        && make install \
        && cd / \
        && rm -fr /usr/src/ss \
        && apk del $buildDeps \
        && rm -rf /var/cache/apk/*

ENV SERVER_ADDR=127.0.0.1 \
    SERVER_PORT=1181  \
    METHOD=chacha20 \
    TIMEOUT=300 \
    PASSWORD=

#------------------------------------------------------------------------------
# Populate root file system:
#------------------------------------------------------------------------------

ADD rootfs /

#------------------------------------------------------------------------------
# Expose ports and entrypoint:
#------------------------------------------------------------------------------
EXPOSE 8123 8124 1188 1181

ENTRYPOINT ["/entrypoint.sh"]
