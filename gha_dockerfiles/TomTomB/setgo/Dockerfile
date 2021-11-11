FROM node:14-alpine

WORKDIR /usr/src/app

ENV PORT 8080
ENV HOST 0.0.0.0

RUN apk add --no-cache git yarn

COPY package*.json ./
COPY decorate-angular-cli.js ./
COPY yarn.lock ./
COPY tools/ ./tools/
COPY .git/ ./.git/

RUN yarn --frozen-lockfile

COPY . .

RUN yarn build:version

RUN yarn build:sw-config

RUN yarn build:ssr:client

RUN yarn build:ssr:server

RUN yarn build:compress

CMD yarn serve:ssr
