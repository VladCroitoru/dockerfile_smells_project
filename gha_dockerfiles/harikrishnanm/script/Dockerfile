FROM rust:1.55 as builder
ENV RUSTFLAGS="-Ctarget-cpu=sandybridge -Ctarget-feature=+aes,+sse2,+sse4.1,+ssse3"
ENV SQLX_OFFLINE=true
WORKDIR /workspace
COPY ./ ./
RUN cargo build --release

FROM debian:buster-slim

RUN apt-get update \
  && apt-get install -y ca-certificates tzdata \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 8088

ENV TZ=Etc/UTC \
  APP_USER=script

RUN groupadd $APP_USER \
  && useradd -g $APP_USER $APP_USER

COPY --from=builder /workspace/target/release/script /
COPY .env /

USER $APP_USER

CMD ["/script"]