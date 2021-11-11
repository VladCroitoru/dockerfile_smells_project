FROM node:6.9

RUN mkdir /app

WORKDIR /app

ADD package.json /app/package.json

ADD index.js /app/index.js

RUN npm install

EXPOSE 3030

CMD node index.js
