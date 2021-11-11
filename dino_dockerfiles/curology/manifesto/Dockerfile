FROM clux/muslrust as compiler

RUN apt-get -y update && apt-get -y install binutils

COPY Cargo.toml Cargo.lock /build/
COPY src/ /build/src/
RUN cd /build && \
    cargo rustc --release --bin manifesto-index -- -C target-cpu=native && \
    cargo rustc --release --bin manifesto-hash -- -C target-cpu=native && \
    cargo rustc --release --bin manifesto-merge -- -C target-cpu=native && \
    strip /build/target/x86_64-unknown-linux-musl/release/manifesto-index && \
    strip /build/target/x86_64-unknown-linux-musl/release/manifesto-hash && \
    strip /build/target/x86_64-unknown-linux-musl/release/manifesto-merge

FROM scratch

COPY --from=compiler /build/target/x86_64-unknown-linux-musl/release/manifesto-index .
COPY --from=compiler /build/target/x86_64-unknown-linux-musl/release/manifesto-hash .
COPY --from=compiler /build/target/x86_64-unknown-linux-musl/release/manifesto-merge .
