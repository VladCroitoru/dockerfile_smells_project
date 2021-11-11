FROM node:14-alpine

RUN mkdir -p /app
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . /app
RUN npm run build

ENV HOST 0.0.0.0
EXPOSE 3000

CMD npm run start
