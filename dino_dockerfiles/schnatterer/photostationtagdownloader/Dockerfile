# Define node version for all stages
# Keep in sync with .github/workflows/build.yaml & createBinaries.js
FROM node:14.15.3-slim as node

FROM node as build

COPY package.json yarn.lock /build/
WORKDIR /build
RUN yarn install

COPY . /build
RUN yarn package linux-x64
RUN mkdir -p /dist/dsdl
RUN mkdir -p /dist/dist
RUN mv dist/dsdl-linux-x64 /dist/dist

# nexe seems to need a couple of libraries
RUN mkdir -p /dist/lib/x86_64-linux-gnu
RUN mkdir -p /dist/usr/lib/x86_64-linux-gnu
RUN cp /lib/x86_64-linux-gnu/libdl.so.2 /dist/lib/x86_64-linux-gnu
RUN cp /lib/x86_64-linux-gnu/librt.so.1 /dist/lib/x86_64-linux-gnu
RUN cp /lib/x86_64-linux-gnu/libgcc_s.so.1 /dist/lib/x86_64-linux-gnu
RUN cp /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /dist/usr/lib/x86_64-linux-gnu

#FROM debian:stretch-20190204-slim (about 95MB), busybox only 45 MB
FROM busybox:1.33.0-glibc

COPY --from=build --chown=1000:1000 /dist /
WORKDIR dsdl

# No need to run as root!
USER 1000:1000

ENTRYPOINT ["/dist/dsdl-linux-x64"]
