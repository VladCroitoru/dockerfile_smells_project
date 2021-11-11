FROM golang:1.7-alpine

ARG PYYAML_VERSION=3.11

# Install dependency packages
RUN set -ex \
    && apk add --update \
           git \
           curl \
    && rm -rf /var/cache/apk/*

# Install Dockerbeat
RUN set -ex \
    && go get github.com/ingensi/dockerbeat \
    && mkdir /etc/dockerbeat \
    && cd $GOPATH/src/github.com/ingensi/dockerbeat \
    && cp etc/dockerbeat.template.json /etc/dockerbeat
COPY dockerbeat.yml /etc/dockerbeat/dockerbeat.yml

# Setup entrypoint
WORKDIR /etc/dockerbeat
COPY entrypoint.sh /etc/dockerbeat/entrypoint.sh
RUN chmod +x /etc/dockerbeat/entrypoint.sh
ENTRYPOINT /etc/dockerbeat/entrypoint.sh
