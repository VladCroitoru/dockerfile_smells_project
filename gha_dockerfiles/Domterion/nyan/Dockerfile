FROM rust:latest
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/nyan
COPY . .
RUN cargo install --path .
CMD ["nyan"]
