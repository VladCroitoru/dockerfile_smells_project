FROM node:14.18.0-alpine3.11

WORKDIR /app

COPY package.json yarn.lock ./

RUN apk add --no-cache build-base python --virtual .build-deps \
  && yarn --production --frozen-lockfile --cache-folder /dev/shm/yarn \
  && apk del .build-deps

COPY next.config.js  ./
COPY .env  ./.env
COPY .next/ ./.next
COPY public/ ./public

USER node

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

CMD ["yarn", "start"]
