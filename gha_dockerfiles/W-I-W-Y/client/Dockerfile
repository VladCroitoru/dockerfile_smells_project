FROM node:latest
USER root

WORKDIR /client
COPY . /client

RUN npm install
COPY . ./

RUN npm run build
