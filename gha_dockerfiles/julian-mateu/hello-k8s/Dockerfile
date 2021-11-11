FROM node:13-alpine

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY ./src ./src

EXPOSE 3000

CMD yarn run serve
