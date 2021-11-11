FROM ubuntu:latest

MAINTAINER Ryan Grothouse

RUN apt-get update
RUN apt-get install -y nodejs npm

# Add code to /software
COPY index.html /software/
COPY server.js /software/
COPY package.json /software/
COPY /public /software/public/

WORKDIR /software/
RUN npm install

EXPOSE 80

CMD nodejs server.js
