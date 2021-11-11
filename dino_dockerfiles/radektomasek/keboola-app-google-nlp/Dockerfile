FROM node:latest
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /tmp

RUN git clone https://github.com/radektomasek/keboola-app-google-nlp ./ && npm install

ENTRYPOINT node index.js /data