FROM node:12.13
MAINTAINER Rogier Slag <rogier@magnet.me>

RUN mkdir /app
ADD package.json /app
RUN cd /app && npm install
ADD index.js /app

WORKDIR /app
CMD ["node", "index.js"]
