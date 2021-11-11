FROM node:16-alpine

WORKDIR /app

COPY package.json /app/

RUN apk update
RUN npm install
RUN apk add bash

CMD ["npm", "start"]