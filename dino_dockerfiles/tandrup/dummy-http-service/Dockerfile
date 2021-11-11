FROM node:8-slim

ADD package.json package.json
RUN npm install

ADD index.js /index.js

EXPOSE 5000

CMD npm start
