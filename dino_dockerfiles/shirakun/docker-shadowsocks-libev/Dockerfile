  
# build for amd64
FROM alpine:latest

MAINTAINER Shira Kagurazaka "nico@ni-co.moe"

RUN apk update \
    && apk add --no-cache build-base git autoconf automake gettext pcre-dev libtool asciidoc xmlto udns-dev c-ares-dev libev-dev libsodium-dev mbedtls-dev linux-headers \
    && git clone https://github.com/shadowsocks/shadowsocks-libev /tmp/shadowsocks-libev \
    && cd /tmp/shadowsocks-libev \
    && git submodule update --init --recursive \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && git clone https://github.com/shadowsocks/simple-obfs.git /tmp/simple-obfs \
    && cd /tmp/simple-obfs && git submodule update --init --recursive \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && apk del build-base git autoconf automake gettext libtool asciidoc xmlto linux-headers \
    && rm -rf /tmp/shadowsocks-libev \
    && rm -rf /tmp/simple-obfs

ENV SERVER_HOST 0.0.0.0
ENV SERVER_PORT 8981
ENV PASSWORD 123456
ENV ENCRYPT_METHOD aes-256-cfb
ENV TIMEOUT 600
ENV DNS_ADDR 8.8.8.8
ENV PLUGIN obfs-server
ENV PLUGIN_OPTS obfs=tls

EXPOSE $SERVER_PORT/tcp $SERVER_PORT/udp

# Start shadowsocks-libev server
ENTRYPOINT ss-server -s "$SERVER_HOST" \
                     -p "$SERVER_PORT" \
                     -k "$PASSWORD" \
                     -m "$ENCRYPT_METHOD" \
                     -t "$TIMEOUT" \
                     -d "$DNS_ADDR" \
                     --plugin "$PLUGIN" \
                     --plugin-opts "$PLUGIN_OPTS" \
                     -u \
                     --reuse-port