# For the moment build release binary first.
# Cargo install takes to long to build container on my
# host - others welcome to build in container
FROM rust:latest as builder
WORKDIR /usr/src/rust-aqi-query
COPY ./target/release/rust-aqi-query . 
# COPY . .
#RUN cargo install --path .

FROM debian:buster-slim
RUN apt-get update && apt-get install -y libssl1.1 
RUN rm -r -f /var/lib/apt/lists/*
COPY --from=builder /usr/src/rust-aqi-query/rust-aqi-query /usr/local/bin/rust-aqi-query
#COPY --from=builder /usr/local/cargo/bin/rust-aqi-query /usr/local/bin/rust-aqi-query
CMD ["rust-aqi-query", "--prometheus-enabled", "true"]
