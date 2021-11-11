# --------------> The build image
#FROM node:latest AS build
FROM node:16-alpine3.14 AS build
WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
RUN --mount=type=secret,mode=0644,id=npmrc,target=/usr/src/app/.npmrc npm ci --only=production

# --------------> The production image
# FROM node:lts-alpine
FROM node:16-alpine3.14
RUN apk add dumb-init
ENV NODE_ENV production
USER node
WORKDIR /usr/src/app
COPY --chown=node:node --from=build /usr/src/app/node_modules /usr/src/app/node_modules
COPY --chown=node:node . /usr/src/app
CMD ["dumb-init", "node", "dist/app.js"]
EXPOSE 3000