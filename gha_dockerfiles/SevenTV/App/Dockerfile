FROM node:12-alpine as builder

WORKDIR /tmp
COPY package.json .
RUN apk update \
    && apk add git yarn curl bash \
    && git clone https://github.com/SevenTV/Typings.git \
    && curl -sfL https://install.goreleaser.com/github.com/tj/node-prune.sh | bash -s -- -b /usr/local/bin \
    && yarn \
    && yarn cache clean

COPY . .

ARG stage

RUN if [[ -z "$stage" ]] ; then yarn build:ssr ; else yarn build-stage:ssr; fi \
    && npm prune --production \
    && /usr/local/bin/node-prune \
    && rm -rf /var/cache/apk/*

FROM node:12-alpine

WORKDIR /app

COPY --from=builder /tmp/dist ./dist

EXPOSE 4000

ENTRYPOINT [ "node", "dist/seventv-app/server/main.js" ]
