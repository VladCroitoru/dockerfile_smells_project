FROM ubuntu:focal

# https://github.com/rust-transit/gtfs-to-geojson.git (rust app)
FROM rust:latest as builder
WORKDIR /
RUN git clone --depth=1 --branch main --single-branch https://github.com/rust-transit/gtfs-to-geojson.git
WORKDIR /gtfs-to-geojson
RUN cargo build --release
RUN strip ./target/release/gtfs-geojson

# https://github.com/etalab/transport-validator.git (rust app)
WORKDIR /
RUN git clone --depth=1 --branch=master --single-branch https://github.com/etalab/transport-validator.git
WORKDIR /transport-validator
RUN cargo build --release
RUN strip ./target/release/main

FROM ubuntu:focal
COPY --from=builder /gtfs-to-geojson/target/release/gtfs-geojson /usr/local/bin/gtfs-geojson
COPY --from=builder /transport-validator/target/release/main /usr/local/bin/transport-validator
RUN apt-get -y update && apt-get -y install libssl-dev
RUN apt-get -y install default-jre
RUN apt-get -y install curl
# https://github.com/MobilityData/gtfs-validator (java app)
RUN curl --location -O https://github.com/MobilityData/gtfs-validator/releases/download/v2.0.0/gtfs-validator-v2.0.0_cli.jar 
# https://github.com/CUTR-at-USF/gtfs-realtime-validator/blob/master/gtfs-realtime-validator-lib/README.md#batch-processing (java app)
RUN curl --location -O https://s3.amazonaws.com/gtfs-rt-validator/travis_builds/gtfs-realtime-validator-lib/1.0.0-SNAPSHOT/gtfs-realtime-validator-lib-1.0.0-SNAPSHOT.jar
