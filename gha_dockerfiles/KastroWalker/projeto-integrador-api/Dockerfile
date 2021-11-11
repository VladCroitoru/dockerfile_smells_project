FROM node:alpine

WORKDIR /usr/app

COPY package*.json ./
RUN npm i && npm cache clean --force

COPY . .

EXPOSE 3000