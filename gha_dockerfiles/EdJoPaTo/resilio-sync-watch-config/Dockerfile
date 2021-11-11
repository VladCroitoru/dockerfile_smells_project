FROM docker.io/resilio/sync AS rslsync



FROM docker.io/library/rust:1-bullseye as builder
WORKDIR /build
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# cargo needs a dummy src/main.rs to detect bin mode
RUN mkdir -p src && echo "fn main() {}" > src/main.rs

COPY Cargo.toml Cargo.lock ./
RUN cargo build --release --locked

# We need to touch our real main.rs file or the cached one will be used.
COPY . ./
RUN touch src/main.rs

RUN cargo build --release --locked


# Start building the final image
FROM docker.io/library/debian:bullseye-slim
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /
VOLUME /folders
VOLUME /.resilio-sync-watch-config
EXPOSE 55555/tcp 55555/udp

RUN ln -sf /run/secrets/share.txt .
COPY --from=rslsync /usr/bin/rslsync /usr/bin/
COPY --from=builder /build/target/release/resilio-sync-watch-config /usr/bin/

ENTRYPOINT ["resilio-sync-watch-config"]
CMD ["single", "--listening-port", "55555"]
