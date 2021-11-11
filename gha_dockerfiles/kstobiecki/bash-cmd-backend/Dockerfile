FROM node:15.11.0-alpine3.13 As production

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}