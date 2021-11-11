FROM thothbot/alpine-jdk8:latest

MAINTAINER Alex Usachev <thothbot@gmail.com>

ENV SBT_VERSION=0.13.15 \
    PATH=${PATH}:/opt/sbt/bin

# do all in one step
RUN set -ex && \
    apk upgrade --update && \
    apk add --update curl && \

    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/sbt.zip \
      https://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.zip && \
    unzip -d /opt /tmp/sbt.zip && \

    ln -s /opt/sbt-launcher-packaging-${SBT_VERSION} /opt/sbt && \
    apk del curl && \

    rm -rf /tmp/* /var/cache/apk/* && \

    sbt sbt-version && \

    mkdir /app

WORKDIR /app