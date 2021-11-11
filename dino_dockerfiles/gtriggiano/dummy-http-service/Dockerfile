FROM mhart/alpine-node:5

MAINTAINER Giacomo Triggiano <giacomo@creativecoding.it>

ADD package.json package.json
RUN npm install

ADD index.js /index.js

EXPOSE 5000

CMD npm start
