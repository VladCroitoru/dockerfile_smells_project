FROM node:7
MAINTAINER Octoblu <docker@octoblu.com>

ENV NPM_CONFIG_LOGLEVEL error

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json yarn.lock /usr/src/app/

RUN yarn install --production

COPY . /usr/src/app

CMD [ "node", "command.js" ]
