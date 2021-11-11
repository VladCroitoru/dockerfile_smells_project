FROM alpine:3.14.2
LABEL maintainer="Moritz Heiber <hello@heiber.im>"
LABEL org.opencontainers.image.source=https://github.com/moritzheiber/alpine-base

ARG ENVCONSUL_VERSION="0.11.0"
ARG ENVCONSUL_SHA256="e52fe2036cacec12b24431044af2c71989c21271ef4d880d3f0e713aee203bc0"
ARG CONSUL_TEMPLATE_VERSION="0.25.1"
ARG CONSUL_TEMPLATE_SHA256="58356ec125c85b9705dc7734ed4be8491bb4152d8a816fd0807aed5fbb128a7b"
ARG GOMPLATE_VERSION="3.8.0"
ARG GOMPLATE_CHECKSUM="847f7d9fc0dc74c33188c2b0d0e9e4ed9204f67c36da5aacbab324f8bfbf29c9"


RUN apk --no-cache upgrade && \
  apk --no-cache add curl ca-certificates && \
  curl -o /tmp/envconsul.zip -L https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip && \
  echo "${ENVCONSUL_SHA256}  /tmp/envconsul.zip" | sha256sum -c - && \
  unzip /tmp/envconsul.zip -d /usr/bin/ && \
  curl -o /tmp/consul-template.zip -L https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
  echo "${CONSUL_TEMPLATE_SHA256}  /tmp/consul-template.zip" | sha256sum -c - && \
  unzip /tmp/consul-template.zip -d /usr/bin/ && \
  curl -o /usr/bin/gomplate -L https://github.com/hairyhenderson/gomplate/releases/download/v${GOMPLATE_VERSION}/gomplate_linux-amd64-slim && \
  echo "${GOMPLATE_CHECKSUM}  /usr/bin/gomplate" | sha256sum -c - && \
  chmod +x /usr/bin/gomplate && \
  rm -f /tmp/envconsul.zip /tmp/consul-template.zip && \
  apk --no-cache del --purge curl
