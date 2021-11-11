# What's this all about?
# See https://snyk.io/blog/10-best-practices-to-containerize-nodejs-web-applications-with-docker/

# --------------> The build image
FROM node:lts AS build
WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
RUN --mount=type=secret,mode=0644,id=npmrc,target=/usr/src/app/.npmrc npm ci --only=production
 
# --------------> The production image
FROM node:lts-alpine
RUN apk add dumb-init --no-cache
ENV NODE_ENV production
USER node
WORKDIR /usr/src/app
COPY --chown=node:node --from=build /usr/src/app/node_modules /usr/src/app/node_modules
COPY --chown=node:node . /usr/src/app
CMD ["dumb-init", "node", "dist/index.js"]
