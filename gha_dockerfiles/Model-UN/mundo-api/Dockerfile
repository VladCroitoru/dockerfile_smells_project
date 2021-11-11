# syntax=docker/dockerfile:1

# PRODUCTION DOCKERFILE
# ---------------------
# Adjusted from: https://github.com/Saluki/nestjs-template/blob/master/Dockerfile
#
# This Dockerfile allows to build a Docker image of the NestJS application
# and based on a NodeJS 14 image. The multi-stage mechanism allows to build
# the application in a "builder" stage and then create a lightweight production
# image containing the required dependencies and the JS build files.
# 
# Dockerfile best practices
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
# Dockerized NodeJS best practices
# https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md
# https://www.bretfisher.com/node-docker-good-defaults/
# http://goldbergyoni.com/checklist-best-practice-of-node-js-in-production/

FROM node:14.17.0 as builder

ENV NODE_ENV build

WORKDIR /app
COPY . /app

RUN npm install -g npm \
    && npm ci \
    && npm run prebuild \
    && npm run build

# -- Production

FROM node:14.17.0

ENV NODE_ENV production
ENV PORT 3000

EXPOSE $PORT

WORKDIR /app
COPY --from=builder /app/package*.json /app/
COPY --from=builder /app/dist/ /app/dist/

RUN npm ci

CMD ["node", "dist/main.js"]

