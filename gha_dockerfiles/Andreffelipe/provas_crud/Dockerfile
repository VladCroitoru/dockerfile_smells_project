FROM node:alpine

USER node
RUN mkdir -p /home/node/app
WORKDIR /home/node/app

COPY --chown=node:node package.json .
COPY --chown=node:node yarn.lock .

RUN yarn --pure-lockfile

COPY --chown=node:node . .

EXPOSE 3000

ENTRYPOINT  ["yarn","start"]
