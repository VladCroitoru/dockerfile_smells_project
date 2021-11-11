FROM rust:1.56.0 AS builder

COPY . /app

WORKDIR /app
RUN cargo build --release

FROM gcr.io/distroless/cc

COPY --from=builder /app/target/release/ddns-cloudflare /

ENTRYPOINT ["/ddns-cloudflare"]
