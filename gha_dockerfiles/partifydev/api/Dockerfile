FROM node:lts-alpine

WORKDIR /usr/src/app

COPY package*.json /usr/src/app/

RUN cd /usr/src/app && npm ci --only=production

COPY . .

EXPOSE 80
CMD [ "node", "index.js" ]
