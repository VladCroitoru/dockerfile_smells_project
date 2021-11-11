# Start with the rust api layer
FROM rust:latest as rust
# Add Dependencies needed for building for alpine
RUN rustup target add x86_64-unknown-linux-musl
RUN apt update && apt install -y musl-tools musl-dev pkg-config libssl-dev
RUN update-ca-certificates
# Copy over our api and build the release
COPY ./api/ /srv/api/
WORKDIR /srv/api
# Set some variables necesary for the build
ARG PKG_CONFIG_ALLOW_CROSS=1
RUN cargo build --target x86_64-unknown-linux-musl --features vendored --release


# Then build our node layer
FROM node:16-alpine as node
WORKDIR /srv
COPY site/package.json site/webpack.env.js site/webpack.prod.js /srv/
RUN npm install --production
COPY site/plugins /srv/plugins/
COPY site/src /srv/src/
RUN npm run build


# Build our final container
FROM alpine:latest
COPY --from=rust /srv/api/target/x86_64-unknown-linux-musl/release/api /srv/api
COPY --from=node /srv/assets /srv/assets
# Temporary, real world would probably download these in the build script
# and make them available to the docker container
COPY api/certs /srv/certs
WORKDIR /srv
CMD ["./api"]
