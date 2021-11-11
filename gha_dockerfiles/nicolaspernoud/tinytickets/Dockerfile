FROM rust as builder
WORKDIR /usr/src/tinytickets
COPY ./backend .
RUN cargo test && \
    cargo install --path .

FROM cirrusci/flutter:stable as frontend-builder
WORKDIR /app
COPY ./frontend .
RUN flutter pub get
RUN flutter test && \
    flutter build web

FROM debian:bullseye-slim
WORKDIR /app
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/cargo/bin/tinytickets_backend /app/tinytickets_backend
COPY --from=builder /usr/src/tinytickets/Rocket.toml /app/Rocket.toml
COPY --from=builder /usr/src/tinytickets/templates/ /app/templates/
COPY --from=frontend-builder /app/build/web/ /app/web/
RUN mkdir -p /app/db/
CMD ["./tinytickets_backend"]