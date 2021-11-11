FROM node:5

MAINTAINER Stanislav Vetlovskiy <mrerliz@gmail.com>

RUN mkdir /app
ADD . /app/

VOLUME ["/tv", "/app/config"]

RUN cd /app && npm install --only=prod

EXPOSE 3000

CMD node /app/src/index.js -w
