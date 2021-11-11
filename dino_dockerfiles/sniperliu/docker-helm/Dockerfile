# The image we keep
FROM alpine:3.6
MAINTAINER Liu Hao <sniperliuhao@gmail.com>

WORKDIR /

ENV HELM_VERSION v2.7.2
ENV HELM_S3_VERSION v0.4.1

# download apk index
RUN apk add --update

RUN apk add --virtual .runtime-utils ca-certificates
RUN apk add --virtual .builtin-utils curl bash

# helm
RUN set -ex \
    && curl -sSL https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar xz \
    && mv linux-amd64/helm /usr/local/bin/helm \
    && rm -rf linux-amd64 \
    && helm init --client-only

# s3 plugins
RUN apk add --virtual .helm-s3-build-deps git make bash \
    && helm plugin install https://github.com/hypnoglow/helm-s3.git --version $HELM_S3_VERSION \
    && apk del --purge .helm-s3-build-deps

# cleanup
RUN apk del --purge .builtin-utils \
    && rm -rf /var/cache/apk/*
