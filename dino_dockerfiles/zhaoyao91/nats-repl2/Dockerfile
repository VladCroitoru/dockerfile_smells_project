FROM node:alpine

ENV NODE_ENV=production

WORKDIR /app

COPY . /app

RUN npm install

CMD node --harmony .