FROM rust:1-buster as rust
FROM node:16-buster as node

FROM rust as rust-deps-mise-en-place
WORKDIR /src
RUN cargo install cargo-chef
COPY . .
RUN cargo chef prepare --recipe-path recipe.json

FROM rust as rust-deps-cook
WORKDIR /src
RUN cargo install cargo-chef
COPY --from=rust-deps-mise-en-place /src/recipe.json recipe.json
RUN cargo chef cook --release --recipe-path recipe.json

FROM node as node-deps-cook
WORKDIR /src/frontend
COPY frontend/package.json frontend/package-lock.json /src/frontend/
RUN npm install

FROM rust as rust-builder
WORKDIR /src
COPY . .
COPY --from=rust-deps-cook /src/target target
COPY --from=rust-deps-cook $CARGO_HOME $CARGO_HOME
RUN cargo build --release --bin brittlq

FROM node as node-builder
WORKDIR /src/frontend
COPY frontend/ .
COPY --from=node-deps-cook /src/frontend/node_modules ./node_modules
RUN npm run build

FROM rust as runtime
WORKDIR /usr/local/bin
COPY --from=rust-builder /src/target/release/brittlq /usr/local/bin
COPY --from=node-builder /src/frontend/dist /usr/local/bin/www/dist
ENTRYPOINT ["/usr/local/bin/brittlq"]
