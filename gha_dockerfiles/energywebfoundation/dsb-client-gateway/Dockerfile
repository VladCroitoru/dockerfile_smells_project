# https://github.com/vercel/next.js/blob/canary/examples/with-docker/Dockerfile

# Install dependencies only when needed
FROM node:14-alpine AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat git
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Rebuild the source code only when needed
FROM node:14-alpine AS builder
WORKDIR /app
COPY . .
COPY --from=deps /app/node_modules ./node_modules
RUN yarn build

# DSB Container
# FROM 098061033856.dkr.ecr.us-east-1.amazonaws.com/ew-dos-dsb-ecr:76dd12d0-6536-4cf4-9f1a-ad90a5366c20

# Independent Container
FROM node:14-alpine as runner

RUN addgroup -g 1001 -S nodejs
RUN adduser -S dsb -u 1001

# RUN mkdir -p /var/deployment/apps/dsb-client-gateway

WORKDIR /var/deployment/apps/dsb-client-gateway
RUN chown dsb /var/deployment/apps/dsb-client-gateway

COPY --from=builder /app/next.config.js ./next.config.js
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/.env ./.env
COPY --from=builder /app/.env.production ./.env.production
COPY --from=builder /app/sentry.client.config.js ./sentry.client.config.js
COPY --from=builder /app/sentry.server.config.js ./sentry.server.config.js
#COPY --from=builder /app/.sentryclirc ./.sentryclirc
RUN chmod +x "./dist/index.js"
USER dsb

RUN echo '{}' > ./in-memory.json

# WORKDIR /var/deployment/apps
#RUN export SENTRY_CLI=./node_modules/.bin/sentry-cli

# COPY --from=builder /app/docker/ecosystem.config.js ./ecosystem.config.js

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1


ENTRYPOINT [ "./dist/index.js" ]
