# 0. BUILD STAGE
FROM ekidd/rust-musl-builder:beta AS build
# only build deps in the first stage for faster builds
COPY Cargo.toml Cargo.toml
USER root
RUN cargo install cargo-build-deps
RUN cargo build-deps --release
RUN rm -f target/x86_64-unknown-linux-musl/release/deps/pektin-api*
# build
ADD --chown=rust:rust . ./
RUN cargo build --release --bin main
RUN strip target/x86_64-unknown-linux-musl/release/main

# 1. APP STAGE
FROM alpine:latest
WORKDIR /app
COPY --from=build /home/rust/src/target/x86_64-unknown-linux-musl/release/main ./pektin-api
# permissions
RUN addgroup -g 1000 pektin-api
RUN adduser -D -s /bin/sh -u 1000 -G pektin-api pektin-api
RUN chown pektin-api:pektin-api pektin-api
USER pektin-api
# run it 
CMD ./pektin-api