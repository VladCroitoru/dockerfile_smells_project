FROM node:alpine as builder

## Install build toolchain, install node deps and compile native add-ons
RUN apk add make curl libcurl gcc g++ python3 net-tools valgrind linux-headers alsa-lib

COPY . .
RUN npm install

FROM node:alpine as app

## Copy built node modules and binaries without including the toolchain
COPY --from=builder node_modules .