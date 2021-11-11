# ------------------------------------------------------------------------------
# Cargo Build Stage
# ------------------------------------------------------------------------------

FROM rust:latest as cargo-build

RUN apt-get update

RUN apt-get install musl-tools -y

RUN rustup target add x86_64-unknown-linux-musl

WORKDIR /usr/src/todo

RUN rm -f target/x86_64-unknown-linux-musl/release/deps/to_do*

COPY . .

RUN RUSTFLAGS=-Clinker=musl-gcc cargo build --release --target=x86_64-unknown-linux-musl
# RUN cargo install --path .
RUN cargo install diesel_cli --no-default-features --features postgres

# ------------------------------------------------------------------------------
# Final Stage
# ------------------------------------------------------------------------------

FROM alpine:latest

RUN apk update
RUN apk add postgresql-client

WORKDIR /home/todo/bin/

RUN addgroup -g 1000 todo
RUN adduser -D -s /bin/sh -u 1000 -G todo todo

COPY --from=cargo-build /usr/src/todo/target/x86_64-unknown-linux-musl/release/todo_* /usr/local/bin/
COPY --from=cargo-build /usr/local/cargo/bin/diesel /usr/local/bin/diesel
COPY ./wait-for.sh ./wait-for.sh

RUN chown todo:todo /usr/local/bin/todo_*

USER todo
