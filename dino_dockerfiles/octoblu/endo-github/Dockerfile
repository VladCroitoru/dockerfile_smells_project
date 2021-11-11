FROM node:5
MAINTAINER Octoblu, Inc. <docker@octoblu.com>

ENV NPM_CONFIG_LOGLEVEL error

EXPOSE 80

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm -s install --production
COPY . /usr/src/app/

CMD [ "node", "command.js" ]
