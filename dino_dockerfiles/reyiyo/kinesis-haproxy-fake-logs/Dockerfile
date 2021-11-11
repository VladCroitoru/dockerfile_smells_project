FROM node:alpine

RUN mkdir /generator
COPY . /generator
WORKDIR /generator

RUN npm i

ENTRYPOINT [ "npm","start" ]