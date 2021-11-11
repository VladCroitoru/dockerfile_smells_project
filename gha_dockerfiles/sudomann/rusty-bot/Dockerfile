#################
#  Build image  #
#################

FROM rust:1.54.0 as build
WORKDIR /tmp/source
COPY Cargo.lock Cargo.toml /tmp/source/
RUN mkdir -p /tmp/source/src && \
  echo "fn main() {}" > /tmp/source/src/main.rs
RUN cargo fetch
RUN cargo build --release

# Dependencies are now cached, copy the actual source code and do another full
# build. The touch on all the .rs files is needed, otherwise cargo assumes the
# source code didn't change thanks to mtime weirdness.
RUN rm -rf /tmp/source/src
COPY src /tmp/source/src
RUN find -name "*.rs" -exec touch {} \; && cargo build --release

##################
#  Output image  #
##################
FROM debian:buster-slim
COPY --from=build /tmp/source/target/release/rusty-bot /usr/local/bin/

ENV RUST_LOG=info
CMD rusty-bot