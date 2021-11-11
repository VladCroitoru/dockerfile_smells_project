FROM rust:1-slim AS builder
WORKDIR /build
COPY ./    ./
RUN cargo build --release

FROM debian:11-slim
COPY --from=builder /build/target/release/postgres-typescript-generator ./
CMD ["./postgres-typescript-generator"]