#
# Dockerfile for shadowsocks-libev with v2ray-plugin
#

FROM alpine AS builder

RUN set -ex \
    # Build environment setup
    && apk add --no-cache --virtual .build-deps \
       autoconf \
       automake \
       build-base \
       c-ares-dev \
       libev-dev \
       libtool \
       asciidoc \
       xmlto \
       libsodium-dev \
       linux-headers \
       mbedtls-dev \
       pcre-dev \
       wget

RUN wget -O - https://api.github.com/repos/shadowsocks/shadowsocks-libev/releases/latest \
    | grep -o "http.*tar.gz" \
    | wget -O /tmp/shadowsocks.tar.gz -i -

RUN mkdir /tmp/shadowsocks-libev
RUN cd /tmp \
    && tar -zxvf shadowsocks.tar.gz --strip-components=1 -C /tmp/shadowsocks-libev

# Build & install
RUN cd /tmp/shadowsocks-libev \
    # && ./autogen.sh \
    && ./configure --prefix=/usr --disable-documentation \
    && make install

FROM golang:1-alpine AS plugin-builder

RUN set -ex && \
    apk add --no-cache git build-base \
    # Build & install
    && wget https://github.com/shadowsocks/v2ray-plugin/archive/master.zip -O /tmp/v2ray-plugin.zip \
    && unzip /tmp/v2ray-plugin.zip -d /tmp \
    && cd /tmp/v2ray-plugin-master \
    && go build

FROM alpine

COPY --from=builder /usr/bin/ss-* /usr/bin/
COPY --from=plugin-builder /tmp/v2ray-plugin-master/v2ray-plugin /usr/bin/

# Runtime dependencies setup
RUN apk add --no-cache \
     rng-tools \
     $(scanelf --needed --nobanner /usr/bin/ss-* \
     | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
     | sort -u)

#USER nobody

#HEALTHCHECK --interval=5s --timeout=3s --retries=12 \
#  CMD ps | awk '{print $4}' | grep v2ray-plugin || exit 1

