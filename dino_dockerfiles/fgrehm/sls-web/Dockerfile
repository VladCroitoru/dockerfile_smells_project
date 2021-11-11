FROM ubuntu:16.04
MAINTAINER Fabio Rehm "fgrehm@gmail.com"

RUN mkdir -p /app \
    && apt-get update \
    && apt-get install -y --no-install-recommends graphviz curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL 'https://github.com/fgrehm/sls-web/releases/download/v0.0.2/sls-web-linux-v0.0.2.tgz' \
    | tar xvz --strip-components 1 -C /app \
    && adduser sls-web

USER sls-web
WORKDIR /app
ENTRYPOINT ["/app/sls-web"]
