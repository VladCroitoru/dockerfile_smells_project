FROM node:lts-slim

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --production --silent

COPY . .
