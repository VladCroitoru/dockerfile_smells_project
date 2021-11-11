FROM rust:1.55 as builder

WORKDIR /usr/src/standup

COPY . .

RUN cargo install --path .

FROM debian:buster-slim

LABEL maintainer="dannypen@gmail.com"

LABEL name="standup"

COPY --from=builder /usr/local/cargo/bin/standup /usr/local/bin/standup

COPY ./assets /usr/local/bin/assets

COPY ./config /usr/local/bin/config

EXPOSE 4200

WORKDIR /usr/local/bin

CMD ["bash", "-c", "standup"]
