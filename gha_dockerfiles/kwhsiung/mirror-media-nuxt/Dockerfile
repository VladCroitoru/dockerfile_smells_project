FROM node:12.16.2-alpine

WORKDIR /app

RUN apk upgrade --no-cache \
    && apk add --no-cache --virtual .build-deps python make g++

COPY package.json .
COPY yarn.lock .
RUN yarn install

ENV NUXT_HOST 0.0.0.0
ENV NUXT_PORT 3000

EXPOSE $NUXT_PORT
CMD [ "yarn", "start" ]

COPY . .

RUN yarn build \
    && apk add --no-cache ca-certificates \
    && apk del .build-deps
