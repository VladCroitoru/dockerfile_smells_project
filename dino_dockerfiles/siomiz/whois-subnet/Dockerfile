FROM node:latest

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

RUN npm install node-whois ip-subnet-calculator

ADD entrypoint.js /entrypoint.js

ENTRYPOINT ["/usr/local/bin/node", "/entrypoint.js"]


