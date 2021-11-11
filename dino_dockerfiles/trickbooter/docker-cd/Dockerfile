FROM node:5.1.0
MAINTAINER Paul Harris <paul@trickbooter.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

EXPOSE 3000

CMD [ "node", "/usr/src/app/app.js" ]

