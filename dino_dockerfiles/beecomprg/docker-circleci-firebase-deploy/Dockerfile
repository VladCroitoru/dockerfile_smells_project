FROM node:8-alpine

RUN apk --no-cache --update upgrade && apk add curl ca-certificates && rm -rf /var/cache/apk/*

RUN npm install -g firebase-tools@latest

#RUN echo `firebase --version`
