# Install dependencies only when needed
FROM node:lts-alpine3.14 AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Rebuild the source code only when needed
FROM node:lts-alpine3.14 AS builder
WORKDIR /app
COPY . .
COPY --from=deps /app/node_modules ./node_modules
RUN NEXT_PUBLIC_BASE_API_URL=BASE_API_URL npm run build && npm install

# Production image, copy all the files and run next
FROM node:lts-alpine3.14 AS runner
WORKDIR /app

ENV NODE_ENV production

RUN addgroup -g 1001 -S nodejs \
 && adduser -S nextjs -u 1001

COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/entrypoint.sh ./entrypoint.sh

RUN ["chmod", "+x", "/app/entrypoint.sh"]

USER nextjs

EXPOSE 3000

ENV NEXT_TELEMETRY_DISABLED 1

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["npm", "run", "start"]