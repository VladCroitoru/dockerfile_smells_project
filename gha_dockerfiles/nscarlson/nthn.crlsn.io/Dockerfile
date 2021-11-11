FROM keymetrics/pm2:8-alpine AS development

# install global dependencies
RUN apk add --no-cache git python make gcc g++ bash

# Set up some configuration
ENV FORCE_COLOR=1
ENV NPM_CONFIG_LOGLEVEL warn

WORKDIR /crlsn

# TODO: move to a script if possible
# Copy project manifests
COPY packages/crlsn-web/package.json ./packages/crlsn-web/

# Copy workspace manifest
COPY .yarnrc package.json yarn.lock ./

# initialize git to temporarily fix an issue with shared-git-hooks
RUN git init

# Install packages
RUN yarn

# # Add chamber CLI for secrets
# ADD https://github.com/segmentio/chamber/releases/download/v2.1.0/chamber-v2.1.0-linux-amd64 /usr/bin/chamber
# RUN chmod 0755 /usr/bin/chamber

# Copy source code
COPY ./ ./

CMD ["sh"]
