FROM node:alpine as base

ARG TZ

ARG ENV

ENV TZ $TZ

WORKDIR /app

COPY package.json yarn.lock ./

RUN npx browserslist@latest --update-db && rm -rf node_modules && yarn install --frozen-lockfile && yarn cache clean

COPY . .

RUN yarn build:$ENV && yarn run build:server

CMD ["node", "./dist/server/core/Server.js"]

FROM base as production
