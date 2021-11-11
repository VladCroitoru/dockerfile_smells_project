FROM rust:buster

WORKDIR /build
COPY . /build

RUN apt -y update && apt install -y libwebkit2gtk-4.0-dev libappindicator3-dev

RUN cargo build --release --features developer

FROM debian:buster

WORKDIR /app
COPY --from=0 /build/target/release/nevermore-fms /app/nevermore-fms

RUN apt -y update && apt install -y libwebkit2gtk-4.0-dev libappindicator3-dev

CMD ["./nevermore-fms"]