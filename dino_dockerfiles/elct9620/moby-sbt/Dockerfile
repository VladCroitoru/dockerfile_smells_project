FROM java:8-jre-alpine

ENV SBT_VERSION 0.13.15
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

RUN apk add --update curl ca-certificates bash && \
    curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built && \
    apk del curl

# Make sure scala-sbt is downloaded
RUN sbt sbtVersion

WORKDIR /app
