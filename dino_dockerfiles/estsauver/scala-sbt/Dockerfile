#
# Scala and sbt Dockerfile
#
# https://github.com/estsauver/scala-sbt
#

# Pull base image
FROM  openjdk:11

ENV SCALA_VERSION 2.12.13
ENV SBT_VERSION 1.4.9


RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Install Scala
## Piping curl directly in tar
RUN \
  case $SCALA_VERSION in \
    "3"*) URL=https://github.com/lampepfl/dotty/releases/download/$SCALA_VERSION/scala3-$SCALA_VERSION.tar.gz SCALA_DIR=/usr/share/scala3-$SCALA_VERSION ;; \
    *) URL=https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz SCALA_DIR=/usr/share/scala-$SCALA_VERSION ;; \
  esac && \
  curl -fsL $URL | tar xfz - -C /usr/share && \
  mv $SCALA_DIR /usr/share/scala && \
  chown -R root:root /usr/share/scala && \
  chmod -R 755 /usr/share/scala && \
  ln -s /usr/share/scala/bin/* /usr/local/bin && \
  case $SCALA_VERSION in \
    "3"*) echo "@main def main = println(util.Properties.versionMsg)" > test.scala ;; \
    *) echo "println(util.Properties.versionMsg)" > test.scala ;; \
  esac && \
  scala test.scala && rm test.scala

RUN \
  curl -fsL "https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz" | tar xfz - -C /usr/share && \
  chown -R root:root /usr/share/sbt && \
  chmod -R 755 /usr/share/sbt && \
  ln -s /usr/share/sbt/bin/sbt /usr/local/bin/sbt
  

RUN apt-get install python python-pip --yes

RUN pip install awscli

# Install rpm for sbt-native-packager
# see https://github.com/hseeberger/scala-sbt/pull/114
RUN apt-get update && \
  apt-get install rpm -y && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /root
