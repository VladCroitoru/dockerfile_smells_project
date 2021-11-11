FROM debian:bullseye-slim@sha256:dddc0f5f01db7ca3599fd8cf9821ffc4d09ec9d7d15e49019e73228ac1eee7f9 AS base

# github metadata
LABEL org.opencontainers.image.source=https://github.com/uwcip/infrastructure-keepalived

# install updates and dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -q update && apt-get -y upgrade && \
    apt-get install -y --no-install-recommends tini keepalived netcat-openbsd && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["tini", "--", "/usr/sbin/keepalived", "--no-syslog", "--dont-fork", "--log-console"]
