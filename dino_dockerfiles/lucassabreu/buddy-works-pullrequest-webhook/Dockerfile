FROM node:7.5.0-alpine

COPY ./ /app/

WORKDIR /app

RUN npm install --production
EXPOSE 8080

ENTRYPOINT node index.js
