FROM node
MAINTAINER Octoblu, Inc. <docker@octoblu.com>

EXPOSE 80
HEALTHCHECK CMD curl --fail http://localhost:80/healthcheck || exit 1

ENV NPM_CONFIG_LOGLEVEL error

WORKDIR /usr/src/app

ADD package.json /usr/src/app/
RUN npm install --production --silent
ADD . /usr/src/app/

CMD node octoblu-flow-canary.js
