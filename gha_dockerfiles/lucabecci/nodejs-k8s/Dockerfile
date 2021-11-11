FROM node:13-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install 

COPY . .
COPY .env .

EXPOSE 8080

CMD node index.js