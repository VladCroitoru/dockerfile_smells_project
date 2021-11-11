FROM debian:jessie
MAINTAINER David Noyes <david@raspberrypython.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y pdns-recursor && \
    apt-get clean && apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 53/tcp 53/udp

ENTRYPOINT ["/usr/sbin/pdns_recursor", "--daemon=no", "--local-address=0.0.0.0"]
