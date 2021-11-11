FROM ekidd/rust-musl-builder:1.49.0 as builder
ADD Cargo.toml Cargo.lock /home/rust/src/
ADD src/ /home/rust/src/src/
RUN cargo check
RUN cargo build --release
RUN strip target/x86_64-unknown-linux-musl/release/tcp_transparent_repeater

FROM alpine
COPY --from=builder /home/rust/src/target/x86_64-unknown-linux-musl/release/tcp_transparent_repeater /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/tcp_transparent_repeater"]
