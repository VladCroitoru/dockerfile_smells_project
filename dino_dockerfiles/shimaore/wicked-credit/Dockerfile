FROM node:alpine

USER root
RUN apk add --no-cache tini
COPY . /src/app
RUN chown -R node /src/app

USER node
WORKDIR /src/app
RUN npm install && npm run prepublish
ENTRYPOINT ["/sbin/tini","--","node","server.js"]
