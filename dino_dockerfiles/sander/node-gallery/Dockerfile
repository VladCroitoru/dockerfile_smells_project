FROM node:0.10
MAINTAINER Sander Dijkhuis <mail@sanderdijkhuis.nl>

COPY . /src
RUN cd /src; npm install

EXPOSE 8080

VOLUME /albums

WORKDIR /src

CMD node server.js
