# syntax=docker/dockerfile:1
FROM rust:1.56-slim AS chef 

WORKDIR /usr/src/integer

RUN set -eux; \
    cargo install cargo-chef; \
    rm -rf $CARGO_HOME/registry

FROM chef as planner

COPY . .
RUN cargo chef prepare --recipe-path recipe.json

FROM chef AS builder

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends libpq-dev; \
    rm -rf /var/lib/apt/lists/*; 

COPY --from=planner /usr/src/integer/recipe.json recipe.json
RUN cargo chef cook --release --recipe-path recipe.json

COPY . .
RUN cargo build --release

FROM debian:bullseye-slim

WORKDIR /usr/local/bin

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends libpq-dev; \
    rm -rf /var/lib/apt/lists/*; 

COPY --from=builder /usr/src/integer/target/release/integer .

ENV TZ Asia/Seoul
ENV ROCKET_ADDRESS 0.0.0.0
EXPOSE 8000
CMD ["./integer"]

