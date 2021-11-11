FROM node:alpine

WORKDIR /usr/app

ADD package.json .
ADD yarn.lock .
RUN yarn install

ADD . .

CMD yarn dev