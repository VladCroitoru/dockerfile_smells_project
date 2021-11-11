FROM node:6
MAINTAINER Octoblu, Inc. <docker@octoblu.com>

EXPOSE 80

ENV NPM_CONFIG_LOGLEVEL error

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm -s install --production
COPY . /usr/src/app/

CMD [ "node", "command.js" ]
