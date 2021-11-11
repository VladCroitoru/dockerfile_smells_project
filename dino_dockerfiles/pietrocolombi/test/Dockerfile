FROM node:carbon
MAINTAINER sviluppatore1
# Create app directory
WORKDIR /usr/src/app

COPY package.json ./

RUN npm install

COPY server.js /usr/src/app

EXPOSE 8080

CMD [ "npm", "start" ]




