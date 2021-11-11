FROM node:alpine
MAINTAINER Froyo Yao <froyo@xenme.com>

RUN apk --no-cache add curl

#Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#fetch app.js and package.json
RUN curl -SLO https://raw.githubusercontent.com/XenMe/adCleaner/master/package.json
RUN curl -SLO https://raw.githubusercontent.com/XenMe/adCleaner/master/app.js

EXPOSE 8123
CMD [ "npm", "start"]
