FROM node:16.11-bullseye-slim as frontend
LABEL org.opencontainers.image.source https://github.com/realaravinth/kaizen
RUN apt-get update && apt-get install -y make
COPY package.json yarn.lock /src/
WORKDIR /src
RUN yarn install
COPY . .
RUN make frontend

FROM rust:1-slim-bullseye as rust
WORKDIR /src
RUN apt-get update && apt-get install -y git
COPY . /src
COPY --from=frontend /src/static/cache/bundle /src/static/cache/bundle
RUN cargo build --release

FROM debian:bullseye-slim
RUN useradd -ms /bin/bash -u 1001 kaizen
WORKDIR /home/kaizen
COPY --from=rust /src/target/release/kaizen /usr/local/bin/
COPY --from=rust /src/config/default.toml /etc/kaizen/config.toml
USER kaizen
CMD [ "/usr/local/bin/kaizen" ]
