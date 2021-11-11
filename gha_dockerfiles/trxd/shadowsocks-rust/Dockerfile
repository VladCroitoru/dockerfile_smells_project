#
# Dockerfile for shadowsocks-rust with v2ray-plugin base on xray-plugin
#

FROM clux/muslrust AS builder

RUN set -ex \
    # Build environment setup
    && apt update \
    && apt install -y \
       wget

RUN wget -O - https://api.github.com/repos/shadowsocks/shadowsocks-rust/releases/latest \
    | grep "tarball_url" | cut -d\" -f4 \
    | wget -O /tmp/shadowsocks-rust.tar.gz -i -

RUN mkdir /tmp/shadowsocks-rust \
    && tar -zxvf /tmp/shadowsocks-rust.tar.gz --strip-components=1 -C /tmp/shadowsocks-rust

ENV RUSTFLAGS="-Ctarget-feature=+aes,+ssse3"

# Build
RUN cd /tmp/shadowsocks-rust \
    && rustup target add x86_64-unknown-linux-musl \
    && cargo build --release --target "x86_64-unknown-linux-musl"

ARG BIN_PATH=/tmp/shadowsocks-rust/target/x86_64-unknown-linux-musl/release

FROM golang:1.16-alpine AS plugin-builder

ARG NAME=xray-plugin

WORKDIR /tmp

RUN set -ex && \
    apk add --no-cache -U git wget build-base \
    && wget -O - "https://api.github.com/repos/teddysun/$NAME/releases/latest" \
       | grep "tarball_url" | cut -d\" -f4 \
       | wget -O /tmp/$NAME.tar.gz -i - \
    && mkdir -p /tmp/$NAME \
    && tar -zxvf /tmp/$NAME.tar.gz --strip-components=1 -C /tmp/$NAME \
    && cd /tmp/$NAME \
    && CGO_ENABLED=0 go build -v -trimpath

FROM gcr.io/distroless/static

ARG BIN_PATH=/tmp/shadowsocks-rust/target/x86_64-unknown-linux-musl/release
COPY --from=builder $BIN_PATH/ssserver /usr/bin/ss-server
COPY --from=builder $BIN_PATH/sslocal /usr/bin/ss-local
COPY --from=plugin-builder /tmp/xray-plugin/xray-plugin /usr/bin/
