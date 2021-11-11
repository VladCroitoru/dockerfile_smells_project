FROM node:14-alpine

RUN apk add --no-cache git
WORKDIR /app
COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile --non-interactive && yarn cache clean

ARG BASE_PATH=""
ARG DEFAULT_NETWORK=""
ARG SUPPORTED_NETWORKS=""

ENV NEXT_TELEMETRY_DISABLED=1 \
  BASE_PATH=$BASE_PATH \
  DEFAULT_NETWORK=$DEFAULT_NETWORK \
  SUPPORTED_NETWORKS=$SUPPORTED_NETWORKS 

COPY . .
RUN yarn build

CMD ["yarn", "start"]
