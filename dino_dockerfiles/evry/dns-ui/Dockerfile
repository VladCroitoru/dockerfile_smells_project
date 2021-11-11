FROM node:8-alpine

WORKDIR /usr/src/app

ADD ./app/package.json .
ADD ./app/yarn.lock .
RUN yarn install --development
ADD ./app .
RUN yarn run grunt && yarn install --production

CMD [ "node", "index.js" ]
