FROM node:4.2
MAINTAINER Rogier Slag <rogier@magnet.me>

RUN touch /opt/privateKey

RUN mkdir /app
ADD package.json /app
RUN cd /app && npm install
ADD index.js /app

WORKDIR /app
CMD ["node", "index.js"]
