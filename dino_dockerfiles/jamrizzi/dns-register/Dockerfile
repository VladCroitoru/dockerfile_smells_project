############################################################
# Dockerfile to run dns-register
# Based on Alpine
############################################################

FROM alpine:3.5

MAINTAINER Jam Risser (jamrizzi)

WORKDIR /app/

ENV CLOUDFLARE_API_KEY=""
ENV CLOUDFLARE_EMAIL=""
ENV CLOUDFLARE_WEBSITE=""
ENV SUBDOMAIN=servers

RUN apk add --no-cache \
        ca-certificates \
        tini && \
    apk add --no-cache --virtual build-deps \
        gcc \
        git \
        go \
        musl-dev \
        openssl

COPY ./ /app/.tmp/
RUN export GOPATH=/app/.tmp/ && \
    export GOBIN=/app/.tmp/bin/ && \
    cd /app/.tmp/ && \
    go get && \
    go build /app/.tmp/dns-register.go && \
    mv /app/.tmp/dns-register /app/dns-register && \
    rm -rf /app/.tmp/ && \
    apk del build-deps

ENTRYPOINT ["/sbin/tini", "--", "/app/dns-register"]
