FROM node:16.10.0-alpine

WORKDIR /app

ENV CI=true
ENV SERVER_PORT=8080
EXPOSE 8080

COPY package*.json .
COPY server.js .
COPY dist dist

RUN npm ci --only=production --ignore-scripts

CMD node server.js