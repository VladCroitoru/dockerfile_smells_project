FROM node

MAINTAINER Genar <genar@acs.li>

COPY . /app

WORKDIR /app

RUN yarn

ENV NODE_ENV production

ENTRYPOINT node app.js
