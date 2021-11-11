FROM amazoncorretto:8-alpine3.14-jre

WORKDIR /opt/docker

COPY package*.json ./

RUN apk update && apk add bash curl npm && npm install && cp -rf node_modules/* /usr/lib/node_modules/
