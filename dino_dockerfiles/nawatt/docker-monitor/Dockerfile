FROM node:6.4.0-slim

MAINTAINER Muhammad Al-Syrwan <mhdsyrwan@gmail.com>

RUN mkdir -p /var/app

WORKDIR /var/app

COPY package.json package.json

RUN npm install

COPY . .

CMD ["npm", "start"]
