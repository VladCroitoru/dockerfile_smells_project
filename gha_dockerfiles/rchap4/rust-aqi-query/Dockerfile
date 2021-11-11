FROM rust:latest as builder
WORKDIR /usr/src
RUN cargo new rust-aqi-query
WORKDIR /usr/src/rust-aqi-query

# cache dependencies
COPY Cargo.toml .
RUN cargo install --path .

COPY . .
RUN touch -a -m ./src/main.rs # forces cargo to rebuild
RUN cargo install --path .

FROM debian:buster-slim
EXPOSE 3030
RUN apt-get update && apt-get install -y libssl1.1 ca-certificates
RUN rm -r -f /var/lib/apt/lists/*
COPY --from=builder /usr/local/cargo/bin/rust-aqi-query /usr/local/bin/rust-aqi-query
CMD ["rust-aqi-query", "--prometheus-enabled", "true"]
