FROM rust:1.55 as builder
WORKDIR /usr/src/rocs
COPY . .
RUN cargo install --path .

FROM debian:buster-slim
COPY --from=builder /usr/local/cargo/bin/rocs /usr/local/bin/rocs
CMD ["rocs"]
