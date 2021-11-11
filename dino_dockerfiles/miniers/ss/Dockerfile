FROM alpine:latest
MAINTAINER miniers

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

RUN buildDeps=" \
                autoconf \
                build-base \
                curl \
                libtool \
                linux-headers \
                openssl-dev \
                pcre-dev \
                tar \
        "; \
        set -x \
        && apk --update --upgrade add openssl pcre \
        && apk add $buildDeps \
        && SS_VERSION=`curl "https://github.com/shadowsocks/shadowsocks-libev/releases/latest" | sed -n 's/^.*tag\/\(.*\)".*/\1/p'` \
        && curl -SL "https://github.com/shadowsocks/shadowsocks-libev/archive/$SS_VERSION.tar.gz" -o ss.tar.gz \
        && mkdir -p /usr/src/ss \
        && tar -xf ss.tar.gz -C /usr/src/ss --strip-components=1 \
        && rm ss.tar.gz \
        && cd /usr/src/ss \
        && ./configure --disable-documentation \
        && make install \
        && cd / \
        && rm -fr /usr/src/ss \
        && apk del $buildDeps \
        && rm -rf /var/cache/apk/*


ENV SERVER_ADDR=0.0.0.0 \
    SERVER_PORT=8388  \
    METHOD=chacha20 \
    TIMEOUT=300 \
    DNS_ADDR=8.8.8.8 \
    OBFS=http\
    PASSWORD=123123321

EXPOSE $SERVER_PORT/tcp
EXPOSE $SERVER_PORT/udp

CMD ss-server -s "$SERVER_ADDR" \
              -p "$SERVER_PORT" \
              -m "$METHOD"      \
              -k "$PASSWORD"    \
              -t "$TIMEOUT"     \
              -d "$DNS_ADDR"    \
              -obfs "$OBFS"    \
              -u                \
              -A                \
              --fast-open $OPTIONS
