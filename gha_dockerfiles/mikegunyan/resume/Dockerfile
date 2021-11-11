# --------------> The build image
FROM node:latest AS build
ARG NPM_TOKEN
WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
RUN echo "//registry.npmjs.org/:_authToken=$NPM_TOKEN" > .npmrc && \
  npm ci --only=production && \
  rm -f .npmrc