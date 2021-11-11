FROM nimmis/alpine:3.4
MAINTAINER ilkka@ilkka.io

RUN apk add --no-cache curl

RUN mkdir -p /tmp/caddy \
 && curl -sL -o /tmp/caddy/caddy_linux_amd64.tar.gz "https://caddyserver.com/download/build?os=linux&arch=amd64" \
 && tar xzf /tmp/caddy/caddy_linux_amd64.tar.gz -C /tmp/caddy \
 && mv /tmp/caddy/caddy /usr/local/bin/ \
 && chmod +x /usr/local/bin/caddy \
 && rm -r /tmp/caddy

ARG docker_gen_version=0.7.3
ENV DOCKER_GEN_VERSION=$docker_gen_version
ENV CADDY_OPTIONS ""

RUN mkdir -p /tmp/docker-gen \
 && curl -sL -o /tmp/docker-gen/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && tar xzf /tmp/docker-gen/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz -C /tmp/docker-gen \
 && mv /tmp/docker-gen/docker-gen /usr/local/bin \
 && chmod +x /usr/local/bin/docker-gen \
 && rm -r /tmp/docker-gen

RUN printf ":80\nproxy / caddyserver.com" > /etc/Caddyfile

ADD etc /etc

ENV DOCKER_HOST unix:///tmp/docker.sock
