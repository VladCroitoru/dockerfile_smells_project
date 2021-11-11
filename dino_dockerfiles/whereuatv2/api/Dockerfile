FROM node:latest
MAINTAINER Scott Kraemer
WORKDIR /var/www

COPY package.json package.json

RUN npm install -g pm2
RUN npm install --silent
COPY . .

RUN mkdir -p /var/log/pm2

RUN apt-get update

EXPOSE 3000

CMD ["node", "server.js"]
