FROM node:0.12-wheezy
MAINTAINER George Rappel
EXPOSE 8080
ADD . /app
WORKDIR /app
RUN npm install
ENTRYPOINT npm start
