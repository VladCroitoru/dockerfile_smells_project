FROM node:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
RUN npm i

COPY . /usr/src/app/

EXPOSE 8080
CMD [ "node", "app.js" ]
