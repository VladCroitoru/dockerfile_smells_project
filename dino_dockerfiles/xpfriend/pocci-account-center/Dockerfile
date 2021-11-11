FROM alpine:3.6
MAINTAINER ototadana@gmail.com

ENV NODEJS_VERSION 6.10.3-r1
ENV NPM_VERSION 6.10.3-r1

RUN apk add --no-cache nodejs=${NODEJS_VERSION} nodejs-npm=${NPM_VERSION} git

COPY ./package.json /pocci-account-center/
RUN cd /pocci-account-center/ && npm install

WORKDIR /pocci-account-center
CMD ["node", "./server.js"]

COPY ./. /pocci-account-center/
RUN ./node_modules/.bin/gulp
