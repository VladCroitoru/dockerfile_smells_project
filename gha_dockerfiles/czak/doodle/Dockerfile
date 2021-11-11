FROM rust:1.42.0-slim-buster as builder
RUN apt-get update && apt-get install -y pkg-config libssl-dev
WORKDIR /usr/src/tools
COPY tools .
RUN cargo install --path .

FROM debian:buster-slim
WORKDIR /checkout
RUN apt-get update && apt-get install -y openssh-client git
RUN mkdir -p ~/.ssh
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts
COPY --from=builder /usr/local/cargo/bin/scribble /usr/local/bin/scribble
COPY --from=builder /usr/local/cargo/bin/estimate /usr/local/bin/estimate
COPY scripts/commit.sh /bin/commit.sh
