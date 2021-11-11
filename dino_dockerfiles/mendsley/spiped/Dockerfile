FROM alpine:3.7 AS builder

RUN apk add --update make g++
RUN apk add openssl-dev
RUN apk add libc6-compat
RUN apk add musl-dev
ADD . /usr/src/spiped
WORKDIR /usr/src/spiped
ARG CC=gcc
ARG BINDIR=/usr/bin
RUN CC=gcc make clean all

FROM alpine:3.7
copy --from=builder /lib/libcrypto.so.1.0.0 /lib/
COPY --from=builder /usr/src/spiped/spiped/spiped /usr/bin/

