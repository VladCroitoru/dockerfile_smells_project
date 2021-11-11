FROM whimsicalbees/docker-java-jdk:1.0
MAINTAINER Whimsical Bees <lena@whimsicalbees.com>

ENV SBT_VERSION 0.13.11
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

RUN curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built

