FROM rust:1.50.0 as build_rust

ARG api_host
ARG api_key
ARG secret_key

ENV API_HOST=$api_host
ENV API_KEY=$api_key
ENV SECRET_KEY=$secret_key
ENV OTP=''
ENV OUTPUT=''

WORKDIR /usr/src/somebdd
COPY . .
RUN cargo build

ENTRYPOINT cargo test -- $API_HOST $API_KEY $SECRET_KEY $OTP $OUTPUT