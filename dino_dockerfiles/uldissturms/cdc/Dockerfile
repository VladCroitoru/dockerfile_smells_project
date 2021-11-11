FROM node:slim
MAINTAINER Uldis Sturms <uldis.sturms@gmail.com>

RUN mkdir -p /usr/app/src
WORKDIR /usr/app/src

RUN npm i cdc --production

ENTRYPOINT ["./node_modules/.bin/cdc"]
