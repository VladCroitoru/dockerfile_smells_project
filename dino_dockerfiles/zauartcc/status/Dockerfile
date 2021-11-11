FROM node:alpine

WORKDIR /usr/src/app

COPY ./dist .
COPY services.json .
COPY package.json .

RUN npm install --prod

CMD node app.js