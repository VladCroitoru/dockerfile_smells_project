FROM geekus/alpine-node-yarn:latest

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json /usr/src/app/

RUN yarn install --production

COPY . /usr/src/app

CMD [ "node", "index.js" ]
