FROM rust:1.55.0-buster AS cargo-generate
RUN apt-get update -qq \
  && apt-get install libssl-dev pkg-config
RUN cargo install cargo-generate

FROM rust:1.42.0-buster

ENV LANG=ja_JP.UTF-8 \
    TZ=Asia/Tokyo \
    USER=root \
    APP_HOME=/usr/src/app

WORKDIR $APP_HOME

RUN rustup default 1.42.0 \
  && rustup component add rustfmt rust-src clippy \
  && curl -L https://github.com/rust-analyzer/rust-analyzer/releases/download/2021-10-04/rust-analyzer-x86_64-unknown-linux-gnu.gz | gunzip -c - > /usr/local/cargo/bin/rust-analyzer \
  && chmod +x /usr/local/cargo/bin/rust-analyzer

COPY --from=cargo-generate /usr/local/cargo/bin/cargo-generate /usr/local/cargo/bin/cargo-generate
