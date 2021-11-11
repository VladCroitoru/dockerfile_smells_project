# Install dependencies only when needed
FROM node:14-alpine AS deps

RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Rebuild the source code only when needed
FROM node:14-alpine AS builder
WORKDIR /app
COPY . .
COPY .env.build .env.local
COPY --from=deps /app/node_modules ./node_modules
RUN yarn install --prefer-offline && yarn build

FROM node:14-alpine AS runner
WORKDIR /app

ENV NODE_ENV production
ENV NEXT_TELEMETRY_DISABLED 1

RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

EXPOSE 3000

COPY --from=builder /app/babel.config.js ./
COPY --from=builder /app/jsconfig.json ./
COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/public ./public
COPY --from=builder /app/pages ./pages
COPY --from=builder /app/.storybook ./.storybook
COPY --from=builder --chown=nextjs:nodejs /app/.next ./.next
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

USER nextjs

CMD ["yarn", "start"]
