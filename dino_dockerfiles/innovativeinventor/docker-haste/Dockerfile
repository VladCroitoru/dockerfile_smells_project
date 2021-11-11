FROM node:9-alpine

MAINTAINER InnovativeInventor

WORKDIR /usr/src/app

RUN apk update && apk upgrade && apk add git
RUN git clone https://github.com/seejohnrun/haste-server /usr/src/app
COPY config.js /usr/src/app/config.js
COPY document_handler.js /usr/src/app/lib/document_handler.js
RUN mkdir ./data

RUN npm install

EXPOSE 7777
CMD [ "npm", "start" ]
