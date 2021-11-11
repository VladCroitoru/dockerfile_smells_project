#
# Dockerfile for shadowsocks-libev
#
FROM s390x/alpine
MAINTAINER ifree.net

ENV SS_VER 3.3.3
ENV SS_URL https://github.com/shadowsocks/shadowsocks-libev/archive/v$SS_VER.tar.gz
ENV SS_DIR shadowsocks-libev-$SS_VER

RUN set -ex apk update && apk upgrade \
    && apk add --no-cache c-ares \
                          openssl \
                          libev \
                          libsodium \
                          mbedtls \
                          pcre \
    && apk add --no-cache \
               --virtual TMP autoconf \
                             automake \
                             build-base \
                             c-ares-dev \
                             curl \
                             gettext-dev \
                             libev-dev \
                             libsodium-dev \
                             libtool \
                             linux-headers \
                             mbedtls-dev \
                             openssl-dev \
                             pcre-dev \
                             tar \
    && curl -sSL $SS_URL | tar xz \
    && cd $SS_DIR \
        && curl -sSL https://github.com/shadowsocks/ipset/archive/shadowsocks.tar.gz | tar xz --strip 1 -C libipset \
        && curl -sSL https://github.com/shadowsocks/libcork/archive/shadowsocks.tar.gz | tar xz --strip 1 -C libcork \
        && curl -sSL https://github.com/shadowsocks/libbloom/archive/master.tar.gz | tar xz --strip 1 -C libbloom \
        && ./autogen.sh \
        && ./configure --disable-documentation \
        && make -j install \
        && cd .. \
        && rm -rf $SS_DIR \
    && apk del TMP

ENV SERVER_ADDR 0.0.0.0
ENV SERVER_PORT 443
ENV METHOD      chacha20
ENV PASSWORD=asdfjkl
ENV DNS_ADDR    176.103.130.130,176.103.130.131

EXPOSE $SERVER_PORT/tcp
EXPOSE $SERVER_PORT/udp


CMD ss-server -s "$SERVER_ADDR" \
              -p "$SERVER_PORT" \
              -m "$METHOD"      \
              -k "$PASSWORD"    \
              -d "$DNS_ADDR"    \
              -u 
