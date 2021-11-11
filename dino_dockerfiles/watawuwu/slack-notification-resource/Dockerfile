FROM watawuwu/rust AS rust-builder

ADD Makefile .
ADD Cargo.toml .
ADD Cargo.lock .

RUN mkdir -p src/bin
RUN echo 'fn main(){}' >  src/bin/in.rs
RUN echo 'fn main(){}' >  src/bin/out.rs
RUN echo 'fn main(){}' >  src/bin/check.rs

RUN make build BUILD_OPTIONS=--release

ADD benches benches
ADD tests tests
ADD src src

RUN make build BUILD_OPTIONS=--release

FROM watawuwu/openssl:latest

RUN mkdir -p /opt/resource

ENV RUST_LOG=info
COPY --from=rust-builder /app/target/x86_64-unknown-linux-musl/release/in /opt/resource
COPY --from=rust-builder /app/target/x86_64-unknown-linux-musl/release/out /opt/resource
COPY --from=rust-builder /app/target/x86_64-unknown-linux-musl/release/check /opt/resource
