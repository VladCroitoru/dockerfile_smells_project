# syntax=docker/dockerfile:1.2
FROM rust:slim-buster as builder

WORKDIR /usr/src/app

COPY ["Cargo.toml", "./"]

COPY ["Cargo.lock", "./"]

COPY ["src/", "./src"]

#COPY ["templates/", "./templates"]

RUN --mount=type=cache,target=/usr/src/app/target \
    --mount=type=cache,target=/usr/local/cargo/registry \
    cargo install --path .



FROM gcr.io/distroless/cc

USER nonroot

COPY templates/ /templates

COPY --from=builder /usr/local/cargo/bin/my_portfolio /

ENTRYPOINT ["/my_portfolio"]
