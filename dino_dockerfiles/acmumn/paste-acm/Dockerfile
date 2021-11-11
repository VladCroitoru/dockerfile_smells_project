FROM rust:1.31
RUN mkdir -p /home/rust/paste-acm
WORKDIR /home/rust/paste-acm
RUN USER=rust cargo init --bin .

COPY ./Cargo.lock ./Cargo.lock
COPY ./Cargo.toml ./Cargo.toml

RUN cargo build --release
RUN rm -rf ./target/release/deps/paste_acm*
RUN rm -rf ./src/*

COPY ./src ./src
RUN cargo build --release

CMD ["/home/rust/paste-acm/target/release/paste-acm", "-vv"]
