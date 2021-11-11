FROM node:9-alpine

ENV NODE_ENV production

WORKDIR /app

COPY app .

RUN apk add --no-cache tini \
 && npm install

ENTRYPOINT ["/sbin/tini", "--"]

CMD [ "node", "index.js", "config.yml" ]