# rust is built with debian slim
FROM rustlang/rust:nightly-slim AS rust-builder

WORKDIR /code
COPY . /code

RUN RUSTFLAGS="-C link-arg=-s" cargo build --release

FROM debian:stable-slim

WORKDIR /code
COPY --from=rust-builder /code/target/release/cosmwasm-simulate /usr/bin/cosmwasm-simulate