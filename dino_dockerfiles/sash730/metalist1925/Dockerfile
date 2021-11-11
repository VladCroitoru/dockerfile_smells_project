FROM node:boron

RUN mkdir /app
WORKDIR /app

COPY package.json /app

RUN npm install --production

ADD /dist /app
