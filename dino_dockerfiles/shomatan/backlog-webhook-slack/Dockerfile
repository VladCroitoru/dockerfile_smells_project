FROM shomatan/sbt:1.0.4-java-8 AS build-env

WORKDIR /work

COPY build.sbt ./
COPY project/* ./project/

RUN sbt update

COPY ./src ./src

RUN set -xe \
    && sbt assembly

# -----------------------------------------------------------------------------
FROM openjdk:8-jre-alpine

MAINTAINER Shoma Nishitateno <shoma416@gmail.com>

RUN set -xe \
    && apk update \
    && apk add --no-cache \
        bash

COPY --from=build-env /work/target/scala-2.12/backlog-webhook-slack-assembly-0.1.0.jar /app/backlog-webhook-slack-assembly.jar

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 9000