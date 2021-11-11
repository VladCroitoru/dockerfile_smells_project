FROM node:7.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
COPY sync.ts /usr/src/app/
RUN npm install && node node_modules/.bin/tsc sync.ts && npm prune --production


EXPOSE 80
CMD [ "node", "/usr/src/app/sync.js" ]
