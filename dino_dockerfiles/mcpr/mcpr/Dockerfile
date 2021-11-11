FROM node:8

MAINTAINER Noah Prail <noah@prail.net>

RUN npm i -g npm@6.1.0

WORKDIR /usr/src/app

COPY package.json .
COPY package-lock.json .

RUN npm ci

COPY . .

EXPOSE 3000
CMD [ "npm", "start" ]