# sbt on OpenJDK 6
#
# Image to build sbt inside a Docker container as described in https://github.com/sbt/sbt/blob/0.13/CONTRIBUTING.md#build-from-source
#
# URL: https://github.com/jaceklaskowski/docker-builds-sbt
#
# If you're reading this and have any feedback on how this image could be improved,
# please open an issue or a pull request so we can discuss it!

FROM jaceklaskowski/docker-sbt-openjdk-6:0.13.9
MAINTAINER Jacek Laskowski <jacek@japila.pl>

ENV SBT_DEV_VERSION 0.13.10
ENV BUILD_PATH      /tmp
ENV SBT_SOURCES     sbt-sources
ENV SBT_SCRIPT      $BUILD_PATH/sbt
ENV SBT_JAR_PATH    /root/.ivy2/local/org.scala-sbt/sbt-launch/$SBT_DEV_VERSION-SNAPSHOT/jars/sbt-launch.jar
ENV PROJECT_DIR     /scala-project
ENV JAVA_HOME       /usr/lib/jvm/java-8-oracle
ENV JAVA_OPTS       "-Xms512M -Xmx1g -Xss1M -XX:+CMSClassUnloadingEnabled -Dfile.encoding=UTF-8 -XX:+UseCompressedOops -XX:NewRatio=9 -XX:ReservedCodeCacheSize=100m"

LABEL description="This image is used to build sbt $SBT_DEV_VERSION from the sources" \
      vendor="Japila Software" \
      version="$SBT_DEV_VERSION"

VOLUME $PROJECT_DIR

WORKDIR $BUILD_PATH

# Build the development version
RUN git clone git://github.com/sbt/sbt.git $SBT_SOURCES && \
  cd $SBT_SOURCES && \
  $SBT_SCRIPT publishLocal && \
  ls -l $SBT_JAR_PATH && \
  cd .. && rm -rf $SBT_SOURCES

WORKDIR $PROJECT_DIR

# Using Java 6
RUN java -jar $SBT_JAR_PATH about

# Install Oracle Java 8
# Copied shamelessly from https://hub.docker.com/r/cloudesire/java/~/dockerfile/
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y --force-yes --no-install-recommends oracle-java8-installer oracle-java8-set-default oracle-java8-unlimited-jce-policy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists && \
    rm -rf /var/cache/oracle-jdk8-installer

ENTRYPOINT $JAVA_HOME/bin/java $JAVA_OPTS -jar $SBT_JAR_PATH
CMD ["help"]
