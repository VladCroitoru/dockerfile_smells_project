# Multi Stage build to get us up and running with the frontend!
# Based on - https://medium.com/hackernoon/a-tale-of-two-docker-multi-stage-build-layers-85348a409c84

ARG NODE_VERSION=14-alpine

FROM node:${NODE_VERSION} AS build

RUN apk --update --no-cache add --virtual native-deps \
  g++ gcc libgcc libstdc++ linux-headers make python libtool autoconf automake

WORKDIR /src
COPY package* ./
RUN npm ci

# Prune out packages and dependencies
RUN npm prune --production && apk del native-deps

# Next Layer!
FROM node:${NODE_VERSION}

# Get curl and bash for healthcheck / waitfor script
RUN apk add --no-cache curl ffmpeg

# Create app directory
WORKDIR /usr/src/app

# Install running deps and get files
COPY --from=build /src/node_modules node_modules
COPY --from=build /src/package* ./

# This will copy all files in our root to the working  directory in the container
# Our precious bot needs to move to the working directory
COPY . ./
# COPY .env ./

HEALTHCHECK --interval=5s \
  --timeout=5s \
  --retries=6 \
  CMD curl -fsI http://localhost:8080/ || exit 1

# Create Port Mappings for website
ENV PORT 8080
EXPOSE 8080

# Image default start strategy
CMD ["npm", "run", "start"]

# docker build -t 127.0.0.1:5000/seth/postie:latest .
# docker push 127.0.0.1:5000/seth/postie:latest
