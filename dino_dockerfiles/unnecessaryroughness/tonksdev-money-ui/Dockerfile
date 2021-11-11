FROM node:8

WORKDIR /home/markt/docker/money/ui

COPY package*.json ./
RUN npm install --only=production

COPY . .

EXPOSE 8080

CMD DEBUG=tonksDEV:* node ./server.js
