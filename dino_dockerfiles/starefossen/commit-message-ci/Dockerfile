FROM node:argon-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD package.json /usr/src/app/
RUN npm install --production

ADD . /usr/src/app
RUN npm run grunt

CMD [ "node", "index.js" ]
