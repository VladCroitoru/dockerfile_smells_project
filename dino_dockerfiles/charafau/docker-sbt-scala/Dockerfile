FROM java:8

ENV SBT_VERSION 0.13.13
ENV SCALA_VERSION 2.11.8
ENV COURSIER_VERSION 1.0.0-M14-7

# scala
RUN \
  curl -fsL http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc

# sbt
RUN \
  curl -L -o sbt-$SBT_VERSION.deb http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt

# ivy2 setup
RUN \
  mkdir -p /root/.sbt/${SBT_VERSION%.*}/plugins && \
  echo 'addSbtPlugin("io.get-coursier" % "sbt-coursier" % "'$COURSIER_VERSION'")' >> /root/.sbt/${SBT_VERSION%.*}/plugins/plugins.sbt && \
  mkdir -p project && \
  echo 'sbt.version='$SBT_VERSION > project/build.properties && \
  echo 'scalaVersion := "'$SCALA_VERSION'"' > build.sbt && \
  sbt

WORKDIR /root
