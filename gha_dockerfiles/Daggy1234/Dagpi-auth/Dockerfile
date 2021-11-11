FROM rust:1.43.1 as build
ENV PKG_CONFIG_ALLOW_CROSS=1

WORKDIR /usr/src/auth_api
COPY . .

RUN cargo install --path .

FROM gcr.io/distroless/cc-debian10

COPY --from=build /usr/local/cargo/bin/auth_api /usr/local/bin/auth_api

CMD ["auth_api"]
