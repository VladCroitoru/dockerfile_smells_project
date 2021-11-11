FROM node:alpine AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json ./
RUN yarn install --frozen-lockfile

FROM node:alpine AS builder
WORKDIR /app
COPY . .
COPY --from=deps /app/node_modules ./node_modules
ENV NODE_OPTIONS=--openssl-legacy-provider
RUN yarn build && yarn install --production --ignore-scripts --prefer-offline

FROM node:alpine AS runner
WORKDIR /app

ENV NODE_ENV production

RUN addgroup -g 1001 -S admin
RUN adduser -S admin -u 1001

COPY --from=builder /app/public ./public
COPY --from=builder --chown=admin:admin /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

USER admin

EXPOSE 3000

CMD ["npm", "run", "start"]
