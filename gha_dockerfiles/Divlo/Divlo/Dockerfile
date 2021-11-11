FROM node:16.8.0 AS dependencies
WORKDIR /usr/src/app
COPY ./package*.json ./
RUN npm clean-install

FROM node:16.8.0 AS builder
WORKDIR /usr/src/app
COPY ./ ./
COPY --from=dependencies /usr/src/app/node_modules ./node_modules
RUN npm run build

FROM node:16.8.0 AS runner
WORKDIR /usr/src/app
ENV NODE_ENV=production
COPY --from=builder /usr/src/app/next.config.js ./next.config.js
COPY --from=builder /usr/src/app/public ./public
COPY --from=builder /usr/src/app/.next ./.next
COPY --from=builder /usr/src/app/i18n.json ./i18n.json
COPY --from=builder /usr/src/app/locales ./locales
COPY --from=builder /usr/src/app/pages ./pages
COPY --from=builder /usr/src/app/node_modules ./node_modules
RUN npx next telemetry disable
CMD ["node_modules/.bin/next", "start", "--port", "${PORT}"]
