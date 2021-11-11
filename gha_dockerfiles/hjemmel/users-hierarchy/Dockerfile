FROM node:12.22.3-alpine

RUN mkdir /app
WORKDIR /app

COPY . .
RUN yarn && yarn cache clean
