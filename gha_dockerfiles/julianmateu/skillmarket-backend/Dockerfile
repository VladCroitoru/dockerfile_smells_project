FROM node:13-alpine

WORKDIR /app

RUN apk add git

COPY package.json package-lock.json ./

RUN npm install

COPY ./src ./src
COPY ./test ./test

EXPOSE 3000

CMD npm run serve
