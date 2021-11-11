FROM rust:1.34.1-stretch

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs

RUN cargo install cargo-web
RUN rustup target add wasm32-unknown-unknown
RUN rustup target add wasm32-unknown-emscripten
RUN cargo web prepare-emscripten

