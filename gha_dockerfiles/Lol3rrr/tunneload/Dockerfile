FROM node:10.19 as web_builder

WORKDIR /usr/src/website

COPY tunneload/src/internal_services/dashboard/website/rollup.config.js ./
COPY tunneload/src/internal_services/dashboard/website/package*.json ./

RUN npm install

COPY tunneload/src/internal_services/dashboard/website ./

RUN npm run build

FROM rust:1.54 as builder

RUN mkdir /tunneload/
COPY . /tunneload/
WORKDIR /tunneload/

RUN rm -rf tunneload/src/internal_services/dashboard/website/public/*
COPY --from=web_builder /usr/src/website/public tunneload/src/internal_services/dashboard/website/public

RUN cargo build --release

FROM debian:buster-slim
ARG APP=/usr/src/app

RUN apt-get update; apt-get upgrade -y; apt-get install libssl1.1 ca-certificates -y

RUN mkdir -p ${APP}

COPY --from=builder /tunneload/target/release/tunneload ${APP}/tunneload

WORKDIR ${APP}

ENTRYPOINT ["./tunneload"]
