# Keep hub.Dockerfile aligned to this file as far as possible

ARG base=hmctspublic.azurecr.io/base/node:12-alpine

# Base image
FROM ${base} as base

USER hmcts

COPY package.json yarn.lock ./
RUN yarn install --production \
    && yarn cache clean

COPY app.js server.js ./
COPY app ./app
COPY config ./config

# Runtime image
FROM base as runtime
ENV PORT 3453
EXPOSE 3453
