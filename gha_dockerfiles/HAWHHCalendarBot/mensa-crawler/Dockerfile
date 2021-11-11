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
    && apt-get install -y bash git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/* /var/log/*

WORKDIR /app
VOLUME /app/meals

COPY gitconfig /root/.gitconfig
COPY known_hosts /root/.ssh/known_hosts
COPY --from=builder /build/target/release/mensa-crawler /usr/bin/

HEALTHCHECK \
    CMD bash -c '[[ $(find . -maxdepth 1 -name ".last-successful-run" -mmin "-250" -print | wc -l) == "1" ]]'

ENTRYPOINT ["mensa-crawler"]
