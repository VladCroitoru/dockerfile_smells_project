FROM node:13-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .
RUN npm install

EXPOSE 3000
CMD node ./start.js