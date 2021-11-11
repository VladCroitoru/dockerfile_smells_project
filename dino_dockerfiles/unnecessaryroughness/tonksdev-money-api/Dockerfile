FROM node:8

WORKDIR /home/markt/docker/money/api

COPY package*.json ./
RUN npm install --only=production

COPY . .

EXPOSE 8081

CMD DEBUG=tonksDEV:* node ./server.js
