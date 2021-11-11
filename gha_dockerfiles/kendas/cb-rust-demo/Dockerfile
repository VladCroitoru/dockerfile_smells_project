FROM rust:alpine AS build

WORKDIR /app

RUN apk add --no-cache musl-dev

COPY ./Cargo.lock ./Cargo.lock
COPY ./Cargo.toml ./Cargo.toml
COPY ./src ./src
COPY ./migrations ./migrations

RUN cargo build --release

FROM alpine

RUN mkdir /app
COPY ./openapi /app/openapi/
COPY --from=build /app/target/release/cb-rust-demo /usr/local/bin/cb-rust-demo

EXPOSE 8080

WORKDIR /app
CMD cb-rust-demo
