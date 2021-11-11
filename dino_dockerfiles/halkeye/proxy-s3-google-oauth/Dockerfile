FROM node:10-alpine
HEALTHCHECK --interval=5m --timeout=3s CMD node bin/healthcheck.js
MAINTAINER Gavin Mogan <docker@gavinmogan.com>
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN NODE_ENV=production npm install
CMD npm run start

