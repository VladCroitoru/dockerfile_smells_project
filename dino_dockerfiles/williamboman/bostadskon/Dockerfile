FROM node:alpine

RUN mkdir -p /src/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app
COPY yarn.lock /usr/src/app
RUN yarn install && yarn cache clean
COPY . /usr/src/app

CMD ["node", "index"]
