FROM node:latest
MAINTAINER Matt Smith <matt@psykzz.co.uk>

RUN mkdir -p /usr/app/
WORKDIR /usr/app

ADD package.json package.json
RUN npm install

ADD . .

CMD node index.js