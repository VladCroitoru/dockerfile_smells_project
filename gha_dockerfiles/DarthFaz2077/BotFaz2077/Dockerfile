FROM --platform=$BUILDPLATFORM rust:1.56.1 AS builder
RUN apt-get update && \
    apt-get install -y gcc-aarch64-linux-gnu \
                       gcc-arm-linux-gnueabihf && \
    rm -rf /var/lib/apt/lists/*
ARG TARGETPLATFORM
RUN echo "Setting cargo target for $TARGETPLATFORM" && \
    case "$TARGETPLATFORM" in \
      linux/amd64) \
        TARGET="x86_64-unknown-linux-gnu"; \
        break;; \
      linux/arm64) \
        TARGET="aarch64-unknown-linux-gnu"; \
        break;; \
      linux/arm/v7) \
        TARGET="armv7-unknown-linux-gnueabihf"; \
        break;; \
      *) echo "Unsupported platform: ${TARGETPLATFORM}!"; exit 1;; \
    esac && \
    echo "$TARGET" > /tmp/target
RUN rustup target add "$(cat /tmp/target)"
WORKDIR /botfaz2077
COPY .cargo/ .cargo/
COPY Cargo.toml Cargo.lock ./
RUN mkdir src && \
    echo 'fn main() {}' > src/main.rs && \
    cargo build --target "$(cat /tmp/target)" --release
COPY . .
RUN touch src/main.rs && \
    cargo build --target "$(cat /tmp/target)" --release && \
    mv target/"$(cat /tmp/target)"/release/botfaz2077 /tmp/botfaz2077

FROM --platform=$TARGETPLATFORM debian:11.1-slim AS runtime
COPY --from=builder /tmp/botfaz2077 /usr/local/bin/
STOPSIGNAL SIGINT
CMD ["/usr/local/bin/botfaz2077"]
