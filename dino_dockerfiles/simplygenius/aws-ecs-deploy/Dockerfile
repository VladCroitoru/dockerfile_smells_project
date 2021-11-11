FROM alpine:latest

RUN apk --update add \
    bash \
    docker \
    jq \
    py-pip \
    python \
    curl \
    zip && \
  pip install awscli && \
  apk --purge del py-pip && \
  rm var/cache/apk/*

COPY scripts/ /usr/local/bin/

RUN mkdir -p /app
VOLUME /app
WORKDIR /app
