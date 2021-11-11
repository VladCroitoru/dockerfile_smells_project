FROM node:10

MAINTAINER SPHERE.IO Support <support@sphere.io>

WORKDIR /app

COPY ./container/files /
COPY . /app

RUN ./container/compile

ENTRYPOINT ["/app/bin/sphere"]
