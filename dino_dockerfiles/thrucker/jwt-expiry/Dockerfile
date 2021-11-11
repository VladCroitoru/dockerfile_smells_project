FROM node:alpine

ADD src/package.json /run/package.json
ADD src/yarn.lock /run/yarn.lock

WORKDIR /run

RUN yarn install

ADD src /run

RUN yarn run build

ENTRYPOINT ["node", "index.js"]
