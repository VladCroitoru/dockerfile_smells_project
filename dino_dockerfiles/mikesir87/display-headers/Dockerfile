FROM node:10-alpine

WORKDIR /usr/src/app/
ADD package.json .
RUN npm install
ADD index.js .
 

EXPOSE 8080

CMD ["node", "/usr/src/app/index.js"]
