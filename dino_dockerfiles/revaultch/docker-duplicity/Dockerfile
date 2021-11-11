FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y duplicity duply python-boto \
    && apt-get clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*

RUN mkdir -p /var/shared

COPY rootfs /
RUN chmod +x /backup.sh
