FROM docker.io/library/debian:11-slim as runtime

ENTRYPOINT ["/usr/local/bin/entrypoint.sh", "gsync"]

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    curl bash git openssh-client libnss-wrapper && \
  rm -rf /var/lib/apt/lists/*

COPY docker/entrypoint.sh /usr/local/bin/
COPY gsync /usr/bin/
USER 1000:0
