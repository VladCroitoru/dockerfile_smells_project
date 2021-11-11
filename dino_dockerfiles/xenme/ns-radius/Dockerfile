FROM node:boron-alpine
MAINTAINER Froyo Yao <froyo@xenme.com>

# add curl
RUN apk --no-cache add curl

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install app dependencies
RUN curl -SLO https://raw.githubusercontent.com/XenMe/ns-radius/master/package.json
RUN npm install

# fetch radius-svr.js
RUN curl -SLO https://raw.githubusercontent.com/XenMe/ns-radius/master/radius-svr.js

EXPOSE 1812/udp

CMD [ "npm", "start"]
