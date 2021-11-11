FROM node:15 AS build-frontend

RUN curl -f https://get.pnpm.io/v6.js | node - add --global pnpm

WORKDIR /app
COPY package.json pnpm-lock.yaml esbuild.js ./
RUN pnpm fetch --prod
RUN pnpm install -r --offline --prod

COPY static static
COPY frontend frontend
RUN pnpm build:frontend

FROM rust:latest AS launch-backend
WORKDIR /app
RUN rustup default nightly
COPY Cargo.toml Cargo.lock ./
COPY src src

RUN --mount=type=cache,target=/usr/local/cargo/registry \
    --mount=type=cache,target=/app/target \
    cargo install --path .

COPY --from=build-frontend /app/static /app/static

CMD [ "crypto-balance" ]