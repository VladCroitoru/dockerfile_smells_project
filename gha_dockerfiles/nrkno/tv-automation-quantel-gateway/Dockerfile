# syntax=docker/dockerfile:experimental
# BUILD IMAGE
FROM node:12

RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    libomniorb4-dev

WORKDIR /opt/quantel-gateway
COPY . .
RUN yarn install --check-files --frozen-lockfile
RUN yarn build
RUN yarn install --check-files --frozen-lockfile --production --force # purge dev-dependencies

# DEPLOY IMAGE
FROM node:12-slim

RUN apt-get update && apt-get install -y \
    libomniorb4-1 curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=0 /opt/quantel-gateway /opt/quantel-gateway
WORKDIR /opt/quantel-gateway

EXPOSE 3000
CMD ["yarn", "start"]
