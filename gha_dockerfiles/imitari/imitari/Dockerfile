FROM rustlang/rust:nightly-alpine as builder
WORKDIR /usr/src/imitari
RUN apk update \
    && apk add --no-cache \
    musl-dev 
COPY . .
RUN cargo install --all-features --path .

FROM alpine:edge
ENV RUST_BACKTRACE=full
RUN apk update \
    && apk add --no-cache \
    ca-certificates \
    musl-dev \
    tini
RUN update-ca-certificates
WORKDIR /usr/local/bin
COPY --from=builder /usr/local/cargo/bin/imitari .
COPY --from=builder /usr/src/imitari/public ./public
COPY --from=builder /usr/src/imitari/templates ./templates
COPY --from=builder /usr/src/imitari/static/ ./static
RUN chmod 777 -R /usr/local/bin/public /usr/local/bin/templates /usr/local/bin/static /usr/local/bin/imitari
CMD ["imitari"]
