FROM node:8-alpine

WORKDIR /usr/src/app

COPY package.json yarn.lock ./
RUN yarn install --ignore-scripts

ADD . .

ENTRYPOINT ["node", "./src/index.js"]
