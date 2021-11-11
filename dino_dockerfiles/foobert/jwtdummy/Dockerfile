FROM node:alpine

WORKDIR /usr/src/app
EXPOSE 3000

RUN apk add --no-cache curl

COPY package.json /usr/src/app
RUN npm install && npm cache clean --force

COPY . /usr/src/app
CMD [ "npm", "start" ]
