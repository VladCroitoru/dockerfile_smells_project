FROM node:16.5-buster AS base
LABEL org.wayscript.image.authors="founders@wayscript.com"

ENV PROJECT_DIR /usr/local/src/project
WORKDIR ${PROJECT_DIR}

COPY package*.json index.js .gitignore ./

RUN npm install

COPY ./files/ /

COPY ./ ${PROJECT_DIR}



RUN chmod u+x /usr/local/bin/*
