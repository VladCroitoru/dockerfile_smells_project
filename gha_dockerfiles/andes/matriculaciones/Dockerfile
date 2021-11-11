ARG NODE_VERSION=10-alpine

FROM node:${NODE_VERSION}
ARG ENVIRONMENT=prod
ENV ENV=${ENVIRONMENT}

ENV node_env=development

RUN apk add --no-cache git

WORKDIR /usr/src/app

COPY package.json package-lock.json   ./ 

RUN npm ci

COPY . .
RUN npm run "build:${ENV}"

