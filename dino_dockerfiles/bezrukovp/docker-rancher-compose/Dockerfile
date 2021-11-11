FROM docker:latest

MAINTAINER Pavel Bezrukov, https://bezr.pro

ENV RANCHER_COMPOSE_VERSION=v0.12.5

ADD ./blue-green-discovery /usr/local/bin/blue-green-discovery

RUN apk add --update python py-pip python-dev && pip install docker-compose && \
    chmod +x /usr/local/bin/blue-green-discovery

RUN apk add --quiet --no-cache ca-certificates curl unzip && \
    curl -sSL "https://github.com/rancher/rancher-compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" | tar -xzp -C /usr/local/bin/ --strip-components=2 && \
    rm -rf /var/cache/*

