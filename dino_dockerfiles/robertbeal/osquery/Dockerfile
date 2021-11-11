FROM debian:stable-slim

ENV VERSION=2.5.0_1
WORKDIR /tmp

RUN apt-get update \
    && apt-get install -y \
        curl \
    && curl -O https://osquery-packages.s3.amazonaws.com/deb/osquery_${VERSION}.linux.amd64.deb \
    && dpkg -i osquery_${VERSION}.linux.amd64.deb \
    && rm -rf /var/lib/apt/lists/* \
    && rm -R /tmp/*

WORKDIR /data
