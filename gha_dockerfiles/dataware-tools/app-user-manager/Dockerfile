# syntax=docker/dockerfile:1.0.0-experimental

FROM node:16.11.1 AS deps
WORKDIR /app
RUN wget -O /bin/jq https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 && chmod +x /bin/jq
COPY . .
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN npm -g config set user root && npm -g config set unsafe-perm true
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm install

FROM docker:20.10.10-dind AS test
RUN apk update && apk add \
  bash \
  git \
  jq \
  nodejs \
  npm
WORKDIR /app
COPY --from=deps /app .
# Update loki config for dind
# See: https://github.com/oblador/loki/issues/9#issuecomment-803197847
RUN rm ./.lokirc.json && mv ./.lokirc-ci.json ./.lokirc.json

# Rebuild the source code only when needed
FROM node:16.11.1-alpine AS builder
WORKDIR /app
COPY . .
COPY --from=deps /app/node_modules ./node_modules
RUN npm run build

# Production image, copy all the files and run next
FROM node:16.11.1-alpine AS production
WORKDIR /app

ENV NODE_ENV production

# You only need to copy next.config.js if you are NOT using the default configuration
COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
RUN chown -R nextjs:nodejs /app/.next
USER nextjs

EXPOSE 3000

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry.
# RUN npx next telemetry disable

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["node_modules/.bin/next", "start"]
