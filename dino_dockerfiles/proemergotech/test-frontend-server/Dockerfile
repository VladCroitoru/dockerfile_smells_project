
FROM node:8-alpine

MAINTAINER Soma Szélpál <szelpalsoma@gmail.com>

RUN mkdir -p /app

ADD . /app

WORKDIR /app

RUN npm install

EXPOSE 8888

CMD [ "npm", "start" ]

