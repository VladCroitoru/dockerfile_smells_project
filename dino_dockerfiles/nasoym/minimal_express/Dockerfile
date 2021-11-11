FROM node:alpine
MAINTAINER Sinan Goo

COPY package.json package.json  
RUN npm install

COPY app.js app.js

EXPOSE 8080

CMD ["npm","start"]  

