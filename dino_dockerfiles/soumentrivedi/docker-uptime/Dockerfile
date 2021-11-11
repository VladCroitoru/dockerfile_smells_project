FROM node:0.12-wheezy
MAINTAINER Soumen Trivedi "soumen.trivedi@arkayaventure.co.uk"

RUN mkdir -p /usr/src && cd /usr/src && git clone git://github.com/fzaninotto/uptime.git && cd uptime && npm install && npm install uptime-webhooks uptime-slack
COPY config/production.yaml /usr/src/uptime/config/
COPY plugins/index.js /usr/src/uptime/plugins/
WORKDIR /usr/src/uptime
ENV NODE_ENV=production
CMD [ "node", "app" ] 