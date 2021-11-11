FROM alpine:3.6

LABEL maintainer="The Idle Developer <theidledeveloper@gmail.com>"

ENV LANG='C.UTF-8' \
    JAVA_HOME='/usr/lib/jvm/java-1.8-openjdk' \
    PATH="$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin" \
    JAVA_VERSION='8u131' \
    JAVA_ALPINE_VERSION='8.131.11-r2'

RUN { \
        echo '#!/bin/sh'; \
        echo 'set -e'; \
        echo; \
        echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
    } > /usr/local/bin/docker-java-home \
    && chmod +x /usr/local/bin/docker-java-home

RUN apk upgrade --update-cache --no-cache --available && \
    apk add --update --update-cache --no-cache \
      openjdk8="${JAVA_ALPINE_VERSION}" && \
    [ "$JAVA_HOME" = "$(docker-java-home)" ]

ENV GATLING_VERSION='2.2.5' \
    GATLING_HOME='/opt/gatling' \
    PATH='/opt/gatling/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

RUN mkdir -p "${GATLING_HOME}" && \
    apk upgrade --update-cache --no-cache --available && \
    apk add --update --update-cache --no-cache \
      wget && \
    mkdir -p /tmp/downloads && \
    wget -q -O "/tmp/downloads/gatling-${GATLING_VERSION}.zip" \
      "https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle/${GATLING_VERSION}/gatling-charts-highcharts-bundle-${GATLING_VERSION}-bundle.zip" && \
    mkdir -p /tmp/archive && cd /tmp/archive && \
    unzip "/tmp/downloads/gatling-${GATLING_VERSION}.zip" && \
    mv /tmp/archive/gatling-charts-highcharts-bundle-${GATLING_VERSION}/* "${GATLING_HOME}/" && \
    rm -rf /tmp/*

WORKDIR "${GATLING_HOME}"

VOLUME ["/opt/gatling/conf", "/opt/gatling/results", "/opt/gatling/user-files"]

ENTRYPOINT ["gatling.sh"]
