FROM node:alpine

RUN apk --no-cache add libc6-compat git python make g++

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
COPY package-lock.json /usr/src/app/
RUN npm install && npm rebuild
RUN npm cache clean --force
COPY . /usr/src/app

CMD [ "npm", "start" ]
