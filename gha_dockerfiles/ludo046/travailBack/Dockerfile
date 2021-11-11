FROM node:14.15.0-alpine

WORKDIR /usr/src/app/back

COPY package*.json ./

RUN npm install --quiet

COPY . .

#EXPOSE 8080

#CMD [ "node", "server.js" ]