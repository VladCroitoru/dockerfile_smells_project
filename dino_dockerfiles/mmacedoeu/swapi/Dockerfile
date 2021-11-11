FROM debian:buster-slim

ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    SQLITE3_LIB_DIR=/usr/lib/x86_64-linux-gnu/libs \
    SQLITE3_INCLUDE_DIR=/usr/include \
    RUSTFLAGS="-C target-cpu=native" \  
    PATH=/usr/local/cargo/bin:$PATH

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        gcc \
        libc6-dev \
        libssl-dev \
        libsqlite3-dev \
        pkg-config \
        make \
        wget \
        git \
        ; \
    \
    url="https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init"; \
    wget "$url"; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --default-toolchain nightly-2018-05-10; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \
    rustup --version; \
    cargo --version; \
    rustc --version; \
    cargo install --git https://github.com/mmacedoeu/swapi; \
    \
    apt-get remove -y --auto-remove \
        wget \
        pkg-config \
        make \
        git \
        ; \
    rm -rf /var/lib/apt/lists/*;

WORKDIR /

CMD ["swapi", "-i", "all", "-l", "warn,actix_web::middleware::logger=warn"]

EXPOSE 8080