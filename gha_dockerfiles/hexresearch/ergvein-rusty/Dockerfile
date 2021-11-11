FROM rust:1 as builder
RUN apt-get update && apt-get install -y clang
COPY . .
RUN cargo build --release

FROM debian:bullseye-slim
COPY --from=builder target/release/ergvein-rusty /usr/local/bin/ergvein-rusty
VOLUME /data
WORKDIR /data
RUN apt update && apt install -y libssl1.1 ca-certificates && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["ergvein-rusty"]
