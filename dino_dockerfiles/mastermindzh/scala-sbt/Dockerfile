FROM  openjdk:8

ENV SCALA_VERSION 2.12.1
ENV SBT_URL http://dl.bintray.com/sbt/debian/sbt-0.13.15.deb

# Install Scala from typesafe.com
RUN \
  curl -fsL http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
  echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc

# Install sbt
RUN \
  curl -L -o sbt.deb $SBT_URL && \
  dpkg -i sbt.deb && rm sbt.deb && \
  apt-get update && apt-get install sbt && \
  sbt sbtVersion

# Install make
RUN \
  apt-get install make

# Define working directory
WORKDIR /opt/project

# No default command.
