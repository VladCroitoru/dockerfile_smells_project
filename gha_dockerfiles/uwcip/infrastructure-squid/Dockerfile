FROM debian:bullseye-slim@sha256:dddc0f5f01db7ca3599fd8cf9821ffc4d09ec9d7d15e49019e73228ac1eee7f9 AS base

# github metadata
LABEL org.opencontainers.image.source=https://github.com/uwcip/infrastructure-squid

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -q update && apt-get -y upgrade && \
    apt-get install -y --no-install-recommends squid squidclient prometheus-squid-exporter && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
COPY entrypoint /entrypoint
RUN chmod +x /entrypoint

HEALTHCHECK --interval=1m --timeout=3s CMD squidclient -h localhost cache_object://localhost/counters || exit 1
ENTRYPOINT ["/entrypoint"]
