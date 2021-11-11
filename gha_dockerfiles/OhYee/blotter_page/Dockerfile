# syntax=docker/dockerfile:experimental

FROM node:16.5.0 AS deps

WORKDIR /data/blotter_page

# deps cache
COPY ./package.json ./yarn.lock ./
RUN yarn install --frozen-lockfile

FROM node:16.5.0 AS builder

WORKDIR /data/blotter_page

# build code
COPY ./ /data/blotter_page
COPY --from=deps /data/blotter_page/node_modules ./node_modules
RUN yarn build && yarn install --production --ignore-scripts --prefer-offline


FROM node:16.5.0 AS prod_deps

WORKDIR /data/blotter_page

# deps cache
COPY ./package.json ./yarn.lock ./
RUN yarn install --frozen-lockfile --prod

FROM node:16.5.0 AS prod

ENV backendURI="http://backend:50000"
WORKDIR /data/blotter_page
ENTRYPOINT [ "yarn", "start" ]

# dev cache
COPY --from=prod_deps /data/blotter_page/package.json /data/blotter_page/yarn.lock ./
COPY --from=prod_deps /data/blotter_page/node_modules ./node_modules

COPY --from=builder /data/blotter_page/next.config.js ./
COPY --from=builder /data/blotter_page/.next ./.next