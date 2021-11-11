FROM node:15-alpine

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 8080
CMD [ "node", "server.js" ]
