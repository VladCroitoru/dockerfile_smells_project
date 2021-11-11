FROM openjdk:8u151-jdk-slim-stretch

RUN apt-get update -y && apt-get install -y curl build-essential checkinstall libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev

RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release

# Scala
ENV SCALA_VERSION 2.12.4

RUN \
  curl -fsL https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo >> /root/.bashrc && \
  echo "export PATH=~/scala-$SCALA_VERSION/bin:$PATH" >> /root/.bashrc

# SBT
ENV SBT_VERSION 1.1.1

RUN \
  curl -L -o sbt-$SBT_VERSION.deb https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  sbt sbtVersion

WORKDIR /root
