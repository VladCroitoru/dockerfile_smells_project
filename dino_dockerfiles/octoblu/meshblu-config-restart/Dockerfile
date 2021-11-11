FROM node:0.10
MAINTAINER MAINTAINER Octoblu Inc. <docker@octoblu.com>

RUN mkdir -p /usr/src/wrapper
WORKDIR /usr/src/wrapper

COPY package.json /usr/src/wrapper/
RUN npm install
COPY . /usr/src/wrapper

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY package.json /usr/src/app/
ONBUILD RUN npm install
ONBUILD COPY . /usr/src/app

CMD [ "node", "/usr/src/wrapper/command.js" ]
