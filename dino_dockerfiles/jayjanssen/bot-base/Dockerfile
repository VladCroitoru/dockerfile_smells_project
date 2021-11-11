FROM node:alpine
MAINTAINER jay.janssen@gmail.com

RUN npm install -g coffee-script nodemon

WORKDIR /bot

RUN npm install bluebird redis winston moment child_process redlock node-vault minimist

COPY src /bot/

USER node

CMD ash