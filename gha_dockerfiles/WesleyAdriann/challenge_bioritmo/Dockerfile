FROM node:12.4-alpine

LABEL maintainer="Wesley Adriann - wesleyadriann@gmail.com"

RUN \
  echo "UPDATING SYSTEM" && \
  apk update && \
  apk add --update

WORKDIR /app

COPY ./package.json .

RUN npm install

COPY . .

EXPOSE 3000

ENTRYPOINT npm start
