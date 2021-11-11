FROM openjdk:8

# FROM java:8

ENV SCALA_VERSION 2.12.6
ENV SBT_VERSION 1.2.1

# Install scala
RUN curl -fsL http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ \
    && echo >> /root/.bashrc \
    && echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc

# Install sbt
RUN curl -L -o sbt-$SBT_VERSION.deb http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb \
    && dpkg -i sbt-$SBT_VERSION.deb \
    && rm sbt-$SBT_VERSION.deb \
    && apt-get update \
    && apt-get install sbt \
    && sbt sbtVersion \
    && apt-get install -y dnsutils build-essential libssl-dev openssl sudo wget

WORKDIR /root
