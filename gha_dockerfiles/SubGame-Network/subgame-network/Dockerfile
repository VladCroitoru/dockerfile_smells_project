FROM rust:1.50.0

RUN apt update && apt install -y \
    cmake \
    pkg-config \
    libssl-dev \
    git \
    build-essential \
    clang \
    libclang-dev \
    curl \
    libz-dev \
    supervisor \
    binaryen

RUN rustup update nightly && \
    rustup update stable && \
    rustup target add wasm32-unknown-unknown --toolchain nightly

WORKDIR /subgame
