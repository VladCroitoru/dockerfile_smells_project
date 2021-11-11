FROM node:latest
WORKDIR /web
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5000
CMD node index.js
