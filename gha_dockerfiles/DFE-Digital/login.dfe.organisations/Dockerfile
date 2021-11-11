FROM node:10

EXPOSE 80

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

RUN mkdir /app
WORKDIR /app

RUN npm install -g nodemon

COPY package*.json ./

RUN npm install

COPY . .

CMD node src/index.js
