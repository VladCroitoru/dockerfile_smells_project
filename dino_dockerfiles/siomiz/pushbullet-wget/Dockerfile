FROM node:latest

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

WORKDIR /opt/pushbullet-wget

RUN npm install pushbullet

ADD main.js /opt/pushbullet-wget/main.js

CMD ["/usr/local/bin/node", "/opt/pushbullet-wget/main.js"]