FROM openjdk:8-alpine
MAINTAINER Ruslan Pilin

ENV SBT_VERSION 1.2.8

ENV SCALA_VERSION 2.12.8

RUN mkdir -p /usr/local/bin && wget -P /usr/local/bin/ https://dl.bintray.com/sbt/maven-releases/org/scala-sbt/sbt-launch/$SBT_VERSION/sbt-launch.jar && ls /usr/local/bin

COPY sbt /usr/local/bin/

# create an empty sbt project;
# then fetch all sbt jars from Maven repo so that your sbt will be ready to be used when you launch the image
COPY init-sbt.sh /tmp/

RUN cd /tmp  && ./init-sbt.sh  && rm -rf *
