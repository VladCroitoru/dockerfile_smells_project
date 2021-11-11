FROM rust:1.50.0 as builder
WORKDIR /usr/src/

# use musl C standard library implementation which allows full static linking
RUN rustup target add x86_64-unknown-linux-musl

# Pre-download binaries by building a project consisting only of Cargo.toml and Cargo.lock
RUN USER=root cargo new mc-server-pinger
WORKDIR /usr/src/mc-server-pinger
COPY Cargo.toml Cargo.lock ./
RUN cargo build --release

# Fully build the app installing it to cargo from which it will later be taken
COPY src ./src
RUN cargo install --target x86_64-unknown-linux-musl --path .

FROM scratch
COPY --from=builder /usr/local/cargo/bin/mc-server-pinger .
ENTRYPOINT ["/mc-server-pinger"]
