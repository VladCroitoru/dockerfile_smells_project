FROM node:lts-alpine AS build
WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
RUN --mount=type=secret,mode=0644,id=npmrc,target=/usr/src/app/.npmrc npm ci --only=production

FROM node:lts-alpine
RUN apk add dumb-init
ENV NODE_ENV production
USER node
WORKDIR /usr/src/node
COPY --chown=node:node --from=build /usr/src/app/node_modules /usr/src/node/node_modules
COPY --chown=node:node . /usr/src/node
