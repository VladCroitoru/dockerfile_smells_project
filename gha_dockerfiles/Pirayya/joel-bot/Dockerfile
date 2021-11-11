FROM rust:1.56.1-buster as builder

RUN rustup override set nightly

RUN mkdir -p /joel-bot

COPY Cargo.toml Cargo.lock /joel-bot/
COPY ./src /joel-bot/src
WORKDIR /joel-bot

# RUN cargo install
RUN cargo build --release

FROM debian:buster
COPY --from=builder /joel-bot/target/release/joel-bot /joel-bot
COPY config.yaml Rocket.toml /
RUN apt update
RUN apt install libssl-dev ca-certificates -y

ENV ROCKET_ENV production

CMD ["/joel-bot"]
