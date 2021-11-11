FROM node:alpine
MAINTAINER Sinan Goo

COPY package.json package.json  
COPY app.js app.js

RUN npm install

EXPOSE 8080

CMD ["npm","start"]  

