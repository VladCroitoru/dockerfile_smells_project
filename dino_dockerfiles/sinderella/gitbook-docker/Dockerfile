FROM node:8.11

RUN apt-get update && apt-get install -y python calibre
RUN npm install gitbook-cli -g
RUN gitbook fetch latest

ADD book.json /

RUN gitbook install

