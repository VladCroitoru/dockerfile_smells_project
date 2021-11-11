FROM node:carbon-alpine@sha256:d75742c5fd41261113ed4706f961a21238db84648c825a5126ada373c361f46e

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --only=production

COPY . .

CMD [ "npm", "start" ]

