FROM node:7.0.0

USER root
WORKDIR /home/app/docker-validator

RUN apt-get update && apt-get install -y openjdk-7-jre openjdk-7-jdk && apt-get clean
RUN npm install -g npm-fast-install

ADD package.json .

RUN npm-fast-install