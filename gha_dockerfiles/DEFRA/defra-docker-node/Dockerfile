# Set default values for build arguments
ARG DEFRA_VERSION=1.2.10
ARG BASE_VERSION=16.13.0-alpine3.14

FROM node:$BASE_VERSION AS production

ARG BASE_VERSION
ARG DEFRA_VERSION

ENV NODE_ENV production

# Set global npm dependencies to be stored under the node user directory
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin
ENV NODE_EXTRA_CA_CERTS=/usr/local/share/ca-certificates/internal-ca.crt

# We need a basic init process to handle signals and reap zombie processes, tini handles that
# Install Internal CA certificate
RUN apk update && apk add --no-cache tini && apk add ca-certificates && rm -rf /var/cache/apk/*
COPY certificates/internal-ca.crt /usr/local/share/ca-certificates/internal-ca.crt
RUN chmod 644 /usr/local/share/ca-certificates/internal-ca.crt && update-ca-certificates

ENTRYPOINT ["/sbin/tini", "--"]

# Never run as root, default to the node user (created by the base Node image)
USER node

# Default workdir should be owned by the default user
WORKDIR /home/node

# Label images to aid searching
LABEL uk.gov.defra.node.node-version=$BASE_VERSION \
      uk.gov.defra.node.version=$DEFRA_VERSION \
      uk.gov.defra.node.repository=defradigital/node

FROM production AS development

ENV NODE_ENV development

LABEL uk.gov.defra.node.repository=defradigital/node-development

# node-gyp is a common requirement for NPM packages. It must be installed as root.
USER root
RUN apk update && \
    apk add --no-cache git && \
    apk add --no-cache --virtual .gyp 'python2=~2.7' make 'g++=~10.3'
# Pact dependencies are not included in Alpine image for contract testing
RUN apk add --no-cache bash wget \
    && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
    && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk \
    && apk add glibc-2.29-r0.apk
USER node
