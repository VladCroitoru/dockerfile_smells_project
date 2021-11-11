FROM rust:1.49

RUN useradd discord
RUN mkdir -p /workspace && mkdir -p /workspace/bin
WORKDIR /workspace
USER discord
RUN cargo install sqlx-cli --no-default-features --features postgres
COPY --chown=discord:discord ./data ./data
COPY --chown=discord:discord ./migrations ./migrations
COPY --chown=discord:discord ./target/x86_64-unknown-linux-musl/release/erebor-record-keeper ./target/x86_64-unknown-linux-musl/release/fetch_scenarios ./target/x86_64-unknown-linux-musl/release/load_challenges ./target/x86_64-unknown-linux-musl/release/kang_csv ./bin/
CMD ["/workspace/bin/erebor-record-keeper"]
