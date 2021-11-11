FROM node:14.17.1-alpine

WORKDIR /opt/app

COPY package*.json ./

RUN npm ci

COPY . .

ENTRYPOINT [ "npm", "start" ]