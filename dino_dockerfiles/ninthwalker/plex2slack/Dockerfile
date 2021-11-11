FROM node:7.7
MAINTAINER ninthwalker

EXPOSE 9889

COPY . /webhooks-slack
WORKDIR /webhooks-slack
RUN npm install
CMD ./index.js
