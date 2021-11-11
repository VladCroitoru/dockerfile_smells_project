FROM openjdk:7-jre

MAINTAINER Peter Salanki <peter@salanki.st>

ENV SBT_VERSION 0.7.7
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

RUN mkdir -p $SBT_HOME/bin
RUN mkdir -p /app

ADD sbt-launch-$SBT_VERSION.jar $SBT_HOME
ADD sbt $SBT_HOME/bin

RUN chmod 755 $SBT_HOME/bin/sbt

WORKDIR /app

#ENTRYPOINT $SBT_HOME/bin/sbt

