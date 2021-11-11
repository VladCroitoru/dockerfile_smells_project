FROM alpine:3.6
MAINTAINER "moalmeida" <moalmeida@koinosystems.com>

RUN apk --update add mongodb mongodb-tools

RUN mkdir -p /data/db

EXPOSE 27017
CMD ["mongod"]
