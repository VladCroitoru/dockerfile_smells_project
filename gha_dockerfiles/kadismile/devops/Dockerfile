FROM node:alpine

RUN mkdir -p /usr/src/NextHandle && chown -R node:node /usr/src/NextHandle

WORKDIR /usr/src/NextHandle

COPY package.json yarn.lock ./

USER node

RUN yarn install --pure-lockfile

COPY --chown=node:node . .

EXPOSE 3000
