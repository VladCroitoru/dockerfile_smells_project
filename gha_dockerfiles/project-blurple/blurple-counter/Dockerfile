FROM node:alpine3.11

WORKDIR /app

RUN apk add python make gcc g++

COPY package*.json .
RUN npm install

COPY . .

CMD ["node", "."]