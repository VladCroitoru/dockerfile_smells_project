FROM frolvlad/alpine-glibc
MAINTAINER Jorn Wijnands <jwijnands@ebay.com>

ENV HEARTBEAT_VERSION=5.3.1

RUN apk add --no-cache \
      ca-certificates \
      curl

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/heartbeat/heartbeat-${HEARTBEAT_VERSION}-linux-x86_64.tar.gz && \
    tar -xvvf heartbeat-${HEARTBEAT_VERSION}-linux-x86_64.tar.gz && \
    mv heartbeat-${HEARTBEAT_VERSION}-linux-x86_64/ /heartbeat && \
    mv /heartbeat/heartbeat.yml /heartbeat/heartbeat.example.yml && \
    mv /heartbeat/heartbeat /bin/heartbeat && \
    chmod +x /bin/heartbeat && \
    mkdir -p /heartbeat/config /heartbeat/data && \
    rm heartbeat-${HEARTBEAT_VERSION}-linux-x86_64.tar.gz

WORKDIR /heartbeat

ADD docker-entrypoint.sh /heartbeat/docker-entrypoint.sh

ENTRYPOINT /heartbeat/docker-entrypoint.sh
