FROM openjdk:8-jdk-alpine

MAINTAINER Fonix Hardcastle, <me@fonix.online>

RUN apk update \
    && apk upgrade \
    && apk add --no-cache --update curl ca-certificates openssl git tar bash sqlite \
    && adduser -D -h /home/container container

USER container
ENV  USER container
ENV  HOME /home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
