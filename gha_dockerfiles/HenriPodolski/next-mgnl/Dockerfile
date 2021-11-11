# Install dependencies only when needed
FROM mhart/alpine-node:16.4.2 AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./
COPY packages/web/package.json  ./packages/web/package.json
COPY packages/lib/package.json  ./packages/lib/package.json
RUN npm ci --workspaces

# Rebuild the source code only when needed
FROM mhart/alpine-node:16.4.2 AS builder
WORKDIR /app
COPY . .
COPY --from=deps /app/node_modules ./node_modules
RUN npm run build:web && npm prune --workspaces --production --ignore-scripts --prefer-offline

# Production image, copy all the files and run next
FROM mhart/alpine-node:16.4.2 AS runner
RUN apk --no-cache add tini
WORKDIR /app

ENV NODE_ENV production

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# You only need to copy next.config.js if you are NOT using the default configuration
# COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/packages/web/public ./packages/web/public
COPY --from=builder --chown=nextjs:nodejs /app/packages/web/.next ./packages/web/.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/packages/web/package.json ./packages/web/package.json
COPY --from=builder /app/packages/web/.env ./packages/web/.env

USER nextjs

EXPOSE 3000

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry.
ENV NEXT_TELEMETRY_DISABLED 1

CMD [ "/sbin/tini", "--", "npm", "run", "start" ]