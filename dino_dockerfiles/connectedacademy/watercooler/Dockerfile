FROM node:8.9.3

# RUN apk --no-cache add git make gcc g++ python

# RUN apk add vips --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

# RUN apt-get update && apt-get install git

RUN npm i --silent -g nodemon

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json

RUN npm i --production --silent

COPY . /usr/src/app

CMD nodemon --exitcrash app.js

EXPOSE 1337