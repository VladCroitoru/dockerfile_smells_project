FROM shomatan/sbt:0.13.15-java-8 AS build-env

WORKDIR /work

COPY build.sbt ./
COPY project/* ./project/

RUN sbt update

COPY ./app  ./app
COPY ./conf ./conf

RUN set -xe \
    && sbt dist \
    && unzip target/universal/ayumi-0.1.0.zip

FROM openjdk:8-jre-alpine

MAINTAINER Shoma Nishitateno <shoma416@gmail.com>

ENV DB_HOST=db DB_NAME=ayumi DB_USER=ayumi DB_PASS=ayumi

RUN set -xe \
    && apk update \
    && apk add --no-cache \
        bash

COPY --from=build-env /work/ayumi-0.1.0 /app

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 9000