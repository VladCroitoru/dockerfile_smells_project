# Based on the labrinth Dockerfile: https://github.com/modrinth/labrinth/blob/master/Dockerfile

FROM rust:1.53

WORKDIR /srv/backend

# Build dependencies first, so that we don't have to wait
# for a full recompile just because a single line in our code changed.

COPY Cargo.toml .
COPY Cargo.lock .
RUN echo "fn main() {}" > dummy.rs
RUN sed -i 's|src/main.rs|dummy.rs|' Cargo.toml
RUN cargo build --release
RUN sed -i 's|dummy.rs|src/main.rs|' Cargo.toml
RUN rm dummy.rs

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

COPY . .

RUN cargo build --release

VOLUME [ "/srv/backend/run" ]

WORKDIR /srv/backend/run

ENV RUST_LOG=info

CMD /wait && /srv/backend/target/release/nucleoid-backend
