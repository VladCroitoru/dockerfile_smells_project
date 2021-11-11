#
# SBT image based on Openjdk 8
#

FROM java:8-jdk-alpine
MAINTAINER Sagacify Devops Team <dev@sagacify.com>

ENV SBT_VERSION 0.13.12
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# Install bash
RUN set -x && apk add --no-cache bash git

# Install sbt
RUN wget -q -O - "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
    mkdir -p ~/.sbt/0.13/plugins && \
    echo 'addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.3")' >> ~/.sbt/0.13/plugins/build.sbt && \
    sbt --about

WORKDIR /app

