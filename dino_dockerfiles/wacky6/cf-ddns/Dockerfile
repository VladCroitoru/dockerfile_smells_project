FROM node:alpine
MAINTAINER Jiewei Qian <qjw@wacky.one>

ADD . .
RUN yarn install

ENTRYPOINT ["bin/cf-ddns"]
