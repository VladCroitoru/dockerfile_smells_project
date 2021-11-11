FROM node:6.4

RUN mkdir -p /usr/node/src/project
WORKDIR /usr/node/src
ADD package.json package.json
RUN npm install -g babel-cli istanbul mocha webpack gulp
RUN npm install
