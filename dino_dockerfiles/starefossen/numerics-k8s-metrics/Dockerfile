FROM node:7-alpine

ENV NODE_ENV production
ENV NPM_CONFIG_LOGLEVEL silent
ENV NPM_CONFIG_PROGRESS false
ENV NPM_CONFIG_SPIN false

WORKDIR /usr/src/app

ADD package.json .
RUN npm install --only=production

ADD index.js .

CMD [ "node", "index.js" ]
