# syntax=docker/dockerfile:1

FROM node:16-alpine

WORKDIR /app

COPY ["package.json", "yarn.lock", "./"]

RUN yarn install --production
RUN yarn global add typescript

COPY . .

RUN yarn build

CMD [ "node", "built/index.js" ]
