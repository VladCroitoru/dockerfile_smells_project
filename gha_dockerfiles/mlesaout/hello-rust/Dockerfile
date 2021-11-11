FROM rust:1.55 as builder
WORKDIR /usr/src/hello-rust
COPY . .
RUN cargo install --path .

FROM debian:buster-slim
COPY --from=builder /usr/local/cargo/bin/hello-rust /usr/local/bin/hello-rust
CMD ["hello-rust"]
