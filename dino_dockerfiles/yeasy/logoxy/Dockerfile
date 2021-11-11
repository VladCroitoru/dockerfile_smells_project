FROM node:6-slim

MAINTAINER Baohua Yang <yeasy.github.io>
ENV TZ Asia/Shanghai
EXPOSE 8080

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install

# Bundle app source
COPY . /usr/src/app

# Only to support development
RUN npm install -g nodemon

CMD [ "npm", "start" ]