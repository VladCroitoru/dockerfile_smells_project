FROM node:6.2.0-slim

RUN mkdir -p /usr/src/
WORKDIR /usr/src/
COPY package.json /usr/src/
RUN npm install --no-progress && npm cache clean
ADD . /usr/src/

ENTRYPOINT ["node_modules/.bin/mocha", "test.js"]
