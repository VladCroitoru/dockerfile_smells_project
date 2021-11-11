FROM ekidd/rust-musl-builder:beta as builder

RUN USER=rust cargo new --bin auth1
WORKDIR /home/rust/src/auth1
COPY ./Cargo.lock ./Cargo.lock
COPY ./Cargo.toml ./Cargo.toml
RUN cargo build --release

RUN rm src/*.rs
ADD . ./
RUN rm ./target/x86_64-unknown-linux-musl/release/deps/auth1*

RUN cargo build --release

FROM alpine:latest

RUN addgroup -S appuser \
    && adduser -S -g appuser appuser

RUN apk update \
	&& apk add --no-cache ca-certificates \
	&& rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

COPY --from=builder /home/rust/src/auth1/target/x86_64-unknown-linux-musl/release/auth1 ./

RUN chown -R appuser:appuser /usr/src/app
USER appuser

EXPOSE 8000
CMD ["./auth1"]
