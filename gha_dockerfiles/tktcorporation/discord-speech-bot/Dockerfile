FROM rust:1.55-slim-buster AS build-env

RUN apt-get update && \
    apt-get install -y \
    libopus-dev \
    build-essential \
    libssl-dev \
    pkg-config \
    autoconf \
    automake \
    libtool \
    m4 \
    ffmpeg \
    curl \
    python \
    git

RUN curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash

RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/bin/youtube-dl && \
    chmod a+rx /usr/bin/youtube-dl

ENV LC_ALL=C.UTF-8

COPY Cargo.lock Cargo.lock
COPY Cargo.toml Cargo.toml

RUN mkdir src/
RUN echo "fn main() {println!(\"if you see this, the build broke\")}" > src/main.rs
RUN cargo build --release
RUN rm -f target/release/deps/discord*

COPY  . .

RUN cargo build --release --features "tts"

CMD [ "/bin/sh",  "-c", "cargo run" ]

FROM debian:buster-20210621-slim

RUN apt-get update && \
    apt-get install -y \
    libopus-dev \
    build-essential \
    libssl-dev \
    pkg-config \
    autoconf \
    automake \
    libtool \
    m4 \
    ffmpeg \
    curl \
    python \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/bin/youtube-dl && \
    chmod a+rx /usr/bin/youtube-dl

ENV LC_ALL=C.UTF-8

COPY --from=build-env /target/release/discord-speech-bot /bin/discord-speech-bot
COPY --from=build-env /sounds /sounds

CMD [ "/bin/sh",  "-c", "discord-speech-bot" ]