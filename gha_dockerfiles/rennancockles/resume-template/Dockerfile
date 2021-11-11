FROM node:lts-alpine

LABEL maintainer="Rennan Cockles <r3ck.dev@gmail.com>"

RUN apk update && apk add git

WORKDIR /app

COPY package.json ./
COPY yarn.lock ./

RUN yarn install

COPY . .
