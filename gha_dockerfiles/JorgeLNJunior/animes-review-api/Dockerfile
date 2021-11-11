FROM node:14-alpine

WORKDIR /usr/app/animes-review-api

RUN apk add --no-cache bash

COPY package*.json ./

RUN npm install --only=prod

RUN npm install pm2@latest -g

COPY public/ ./public/

COPY wait-for-it.sh ./

RUN chmod +x ./wait-for-it.sh
