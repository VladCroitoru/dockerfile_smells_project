FROM ubuntu:xenial

LABEL maintainer BITWORKS

ENV version 1.3.8.0-SNAPSHOT
ENV slf4j_version 1.7.24

ENV DEBIAN_FRONTEND noninteractive

# Install Oracle JDK 8
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
    apt-get install -y --no-install-recommends oracle-java8-installer && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated --no-install-recommends sbt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# see .dockerignore in root dir
COPY ./project /opt/bin/tts/project
COPY ./build.sbt /opt/bin/tts/
COPY ./src/main /opt/bin/tts/src/main
COPY ./rundocker.sh /opt/

WORKDIR /opt/bin/tts

RUN mkdir -p /root/.sbt/0.13

RUN sbt 'set test in assembly := {}' clean assembly

RUN mv target/scala-2.12/tstreams-transaction-server-${version}.jar . && \
    mv /root/.ivy2/cache/org.slf4j/slf4j-api/jars/slf4j-api-${slf4j_version}.jar . && \
    mv /root/.ivy2/cache/org.slf4j/slf4j-log4j12/jars/slf4j-log4j12-${slf4j_version}.jar . && \
    sbt clean clean-files && \
    rm -rf /root/.ivy2/cache

WORKDIR /var/log/tts
ENTRYPOINT /opt/rundocker.sh /etc/conf/config.properties ${version} ${slf4j_version}

