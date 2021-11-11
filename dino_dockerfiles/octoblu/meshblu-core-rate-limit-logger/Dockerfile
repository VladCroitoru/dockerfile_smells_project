FROM node:6
MAINTAINER Octoblu <docker@octoblu.com>

ENV NPM_CONFIG_LOGLEVEL error
ENV NODE_ENV production

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN npm install --silent --global yarn

COPY package.json yarn.lock /usr/src/app/

RUN yarn install

COPY . /usr/src/app

CMD [ "node", "command.js" ]
