FROM rust:1.56-buster as builder
ENV STATIC_DIR=/var/www/before
WORKDIR /usr/src/before
COPY . .
RUN cargo install --path .
RUN objcopy --compress-debug-sections /usr/local/cargo/bin/before

FROM debian:buster-slim
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/cargo/bin/before /usr/local/bin/before
COPY --from=builder /usr/src/before/static /var/www/before
CMD ["before"]
