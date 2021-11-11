ARG VERSION=1.0.0

FROM rust:slim AS builder
RUN apt-get update -yqq && apt-get install -yqq git wget musl-tools build-essential ca-certificates

ARG VERSION
ARG RUST_TARGET

RUN wget -O- https://api.github.com/repos/geph-official/geph4/tags \
    | grep "tarball_url" | cut -d\" -f4 | head -n1 \
    | wget -O /tmp/geph.tar.gz -i -

ENV WD=/tmp/geph
WORKDIR $WD

RUN tar -zxvf /tmp/geph.tar.gz --strip-components=1 -C "$WD" \
    && export PATH=$HOME/.cargo/bin:$PATH \
    && rustup target add x86_64-unknown-linux-musl \
    && cargo build --release --target x86_64-unknown-linux-musl \
    && mv ./target/x86_64-unknown-linux-musl/release/geph4-client /tmp/geph4-client-linux-amd64

FROM alpine

RUN apk add --no-cache -U ca-certificates; \
    rm -rf /var/cache/apk/*

COPY --from=builder /tmp/geph4-client-linux-amd64 /usr/local/bin/geph4

ENV USERNAME=""
ENV PASSWORD=""

CMD ["/usr/local/bin/geph4", "connect", "--username", "$USERNAME", "--password", "$PASSWORD"]
