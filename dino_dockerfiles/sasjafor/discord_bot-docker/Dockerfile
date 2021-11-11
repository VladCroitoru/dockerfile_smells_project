FROM rust:1.52 as builder

# Create empty shell project
RUN USER=root cargo new --bin announcer_bot

WORKDIR /announcer_bot

# Copy manifest
COPY ./Cargo.toml ./Cargo.toml

# Build dependencies
RUN RUSTFLAGS='-C link-arg=-s' cargo build --release

RUN rm src/*.rs

ADD . ./

# Build for release
RUN rm ./target/release/deps/announcer_bot*
RUN RUSTFLAGS='-C link-arg=-s' cargo build --release

FROM debian:buster-slim

# Set log level
ENV RUST_LOG warn

# Setup apt, install package dependencies and create /config
RUN apt-get update && \
    apt-get install -y --no-install-recommends  ca-certificates \
                                                espeak \
                                                ffmpeg \
                                                lame \
                                                libopus0 \
                                                libsqlite3-dev \
                                                libssl-dev \
                                                python \
                                                vorbis-tools \
                                                && \
    mkdir /config

# Copy run script
COPY src/run /bin

# Copy executable
COPY --from=builder /announcer_bot/target/release/announcer_bot /bin

WORKDIR /

# Install youtube-dl
ADD https://yt-dl.org/downloads/latest/youtube-dl /usr/local/bin/
RUN chmod a+rx /usr/local/bin/youtube-dl

# Set run command
VOLUME /config
CMD ["run"]
