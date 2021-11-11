FROM node:7.2.1

MAINTAINER Mikhail Faraponov

RUN mkdir /app

WORKDIR /app

COPY package.json /app/package.json

RUN npm install --no-optional && npm install nodemon -g --no-optional

COPY . /app

CMD nodemon -L
