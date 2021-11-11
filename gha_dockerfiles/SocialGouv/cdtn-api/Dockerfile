FROM node:14.17.6-alpine

RUN apk add --no-cache git

ARG PORT
ARG REDIS_URL

ENV NODE_ENV=production
ENV PORT=$PORT
ENV REDIS_URL=$REDIS_URL

WORKDIR /app

COPY package.json yarn.lock /app/

RUN yarn --frozen-lockfile

COPY src /app/src

USER node

ENTRYPOINT ["yarn", "start"]
