FROM node:14-alpine AS builder
RUN apk add --update bash git
RUN rm -rf /var/cache/apk/*
WORKDIR /usr/src/app

COPY ./yarn.lock ./yarn.lock
COPY ./package.json ./package.json
RUN yarn cache clean
RUN yarn install --frozen-lockfile --check-files

COPY ./src ./src
COPY ./next.config.js ./next.config.js
COPY ./next-env.d.ts ./next-env.d.ts
COPY ./.eslintrc ./.eslintrc
COPY ./public ./public
COPY ./tsconfig.json ./tsconfig.json

ARG CAISY_API_KEY
ARG CAISY_ORGANIZATION_ID

ENV CAISY_API_KEY $CAISY_API_KEY
ENV CAISY_ORGANIZATION_ID $CAISY_ORGANIZATION_ID

ENV NODE_ENV production
CMD yarn build && yarn start 
