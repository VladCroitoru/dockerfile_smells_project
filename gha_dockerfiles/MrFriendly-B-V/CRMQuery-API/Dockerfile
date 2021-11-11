FROM docker-registry.k8s.array21.dev/openssl-musl:latest AS OPENSSL

# Program builder
FROM rust:1.53.0-bullseye as BUILDER
RUN apt update && apt install -y \
    musl-tools \
    pkgconf

RUN rustup target add x86_64-unknown-linux-musl

COPY ./src /usr/src/crm_query/src/
COPY ./Cargo.toml /usr/src/crm_query/

COPY --from=OPENSSL /musl /musl

WORKDIR /usr/src/crm_query/

ENV PKG_CONFIG_ALLOW_CROSS=1
ENV OPENSSL_STATIC=true
ENV OPENSSL_DIR=/musl

ENV RUSTFLAGS='-C link-arg=-s'
RUN cargo build --release --target x86_64-unknown-linux-musl

# Runtime image
FROM alpine:latest
RUN apk add --no-cache ca-certificates
COPY --from=BUILDER /usr/src/crm_query/target/x86_64-unknown-linux-musl/release/crm_query /usr/local/bin/crm_query
COPY ./log4rs.yaml /usr/local/bin/

RUN chmod a+rx /usr/local/bin/*
RUN adduser crm_query -s /bin/false -D -H
USER crm_query

EXPOSE 8080
WORKDIR /usr/local/bin
ENTRYPOINT [ "/usr/local/bin/crm_query" ]