FROM node:latest
MAINTAINER timdelgado@gamestop.com

COPY . /app
WORKDIR /app

RUN npm install -g mocha && \
    npm install

ENTRYPOINT ["mocha"]