FROM node:latest
MAINTAINER Svetlana Linuxenko <linuxenko@yahoo.com>

RUN mkdir /app
WORKDIR /app

ADD package.json /app/package.json
ADD index.js /app/index.js

RUN npm install

EXPOSE 3000

CMD ["node", "index.js"]