FROM node:0.12.17-wheezy

WORKDIR /data

ADD ["package.json", "npm-shrinkwrap.json", "/data/"]

RUN npm install --global grunt-cli && npm install
