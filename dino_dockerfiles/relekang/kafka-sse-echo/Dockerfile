FROM node:8-alpine

EXPOSE 3000

WORKDIR /app

COPY package.json .
COPY yarn.lock .

RUN yarn

COPY index.js .

CMD ./node_modules/.bin/micro index.js
