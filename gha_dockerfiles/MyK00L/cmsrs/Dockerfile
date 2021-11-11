### build base ###
FROM rust:1.55.0-slim AS chef
USER root
RUN rustup default nightly-2021-10-05
RUN rustup component add rustfmt
RUN cargo install cargo-chef
RUN apt-get update && apt-get install libseccomp-dev lld -y
WORKDIR /src

### prepares chef for workspace ###
FROM chef AS planner
COPY . .
RUN mv /src/.cargo/config.toml.dockerfast /src/.cargo/config.toml
RUN cargo chef prepare --recipe-path recipe.json

### builds workspace ###
FROM chef AS builder
COPY --from=planner /src/recipe.json recipe.json
RUN cargo chef cook --recipe-path recipe.json # --release
COPY . .
RUN cargo build --workspace # --release

### CONTEST SERVICE ###
FROM debian:buster-slim AS contest_service
COPY --from=builder /src/target/debug/contest_service /usr/local/bin/
EXPOSE 50051
ENTRYPOINT ["/usr/local/bin/contest_service"]

### EVALUATION SERVICE ###
FROM debian:buster-slim AS evaluation_service
COPY --from=builder /src/target/debug/evaluation_service /usr/local/bin/
EXPOSE 50051
ENTRYPOINT ["/usr/local/bin/evaluation_service"]

### DISPATCHER SERVICE ###
FROM debian:buster-slim AS dispatcher_service
COPY --from=builder /src/target/debug/dispatcher_service /usr/local/bin/
EXPOSE 50051
ENTRYPOINT ["/usr/local/bin/dispatcher_service"]

### SUBMISSION SERVICE ###
FROM debian:buster-slim AS submission_service
COPY --from=builder /src/target/debug/submission_service /usr/local/bin/
EXPOSE 50051
ENTRYPOINT ["/usr/local/bin/submission_service"]

### WORKER SERVICE ###
FROM debian:buster-slim AS worker_service
COPY --from=builder /src/target/debug/worker_service /usr/local/bin/
EXPOSE 50051
RUN groupadd -g 1000 user && useradd -m -g 1000 -u 1000 user
ENTRYPOINT ["/usr/local/bin/worker_service"]

### ADMIN ###
FROM debian:buster-slim AS admin
RUN apt-get update && apt-get install openssl -y
COPY --from=builder /src/target/debug/admin /usr/local/bin/
COPY --from=builder /src/admin /src/admin
WORKDIR /src/admin
RUN sh ./gen_secrets.sh 2>/dev/null
ENV ROCKET_PORT=80
ENTRYPOINT ["/usr/local/bin/admin"]

### PARTICIPANT ###
FROM debian:buster-slim AS participant
RUN apt-get update && apt-get install openssl -y
COPY --from=builder /src/target/debug/participant /usr/local/bin/
COPY --from=builder /src/participant /src/participant
WORKDIR /src/participant
RUN sh ./gen_secrets.sh 2>/dev/null
ENV ROCKET_PORT=80
ENTRYPOINT ["/usr/local/bin/participant"]

