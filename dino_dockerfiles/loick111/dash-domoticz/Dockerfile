FROM node:7.7.4-alpine

MAINTAINER Loïck MAHIEUX <loick@loick.fr>

RUN apk update && apk upgrade && \
    apk add --no-cache git python libpcap-dev g++ make

RUN mkdir -p /app
WORKDIR /app

COPY package.json /app
RUN npm install

COPY src /app/src
COPY config /app/config

CMD [ "npm", "start" ]