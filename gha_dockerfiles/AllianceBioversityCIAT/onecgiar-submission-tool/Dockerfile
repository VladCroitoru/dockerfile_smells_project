FROM node:10-alpine

WORKDIR /usr/src/app

COPY one-cgiar-back/package*.json ./

RUN npm i --production --silent

COPY one-cgiar-back/ .

COPY one-cgiar-front/dist /usr/src/one-cgiar-front/dist

EXPOSE 3000

CMD [ "node", "dist/index.js" ]
