FROM openjdk:8

MAINTAINER sunny94

# Scala related variables.
ARG SCALA_VERSION=2.10.4
ARG SCALA_BINARY_ARCHIVE_NAME=scala-${SCALA_VERSION}
ARG SCALA_BINARY_DOWNLOAD_URL=http://downloads.lightbend.com/scala/${SCALA_VERSION}/${SCALA_BINARY_ARCHIVE_NAME}.tgz

# SBT related variables.
ARG SBT_VERSION=0.13.8
ARG SBT_BINARY_ARCHIVE_NAME=sbt-$SBT_VERSION
ARG SBT_BINARY_DOWNLOAD_URL=https://dl.bintray.com/sbt/native-packages/sbt/${SBT_VERSION}/${SBT_BINARY_ARCHIVE_NAME}.tgz

# Spark related variables.
ARG SPARK_VERSION=1.6.2
ARG SPARK_BINARY_ARCHIVE_NAME=spark-${SPARK_VERSION}-bin-hadoop2.6
ARG SPARK_BINARY_DOWNLOAD_URL=http://d3kbcqa49mib13.cloudfront.net/${SPARK_BINARY_ARCHIVE_NAME}.tgz

# Configure env variables for Scala, SBT and Spark.
# Also configure PATH env variable to include binary folders of Java, Scala, SBT and Spark.
ENV SCALA_HOME  /usr/local/scala
ENV SBT_HOME    /usr/local/sbt
ENV SPARK_HOME  /usr/local/spark
ENV PATH        $JAVA_HOME/bin:$SCALA_HOME/bin:$SBT_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

# Download, uncompress and move all the required packages and libraries to their corresponding directories in /usr/local/ folder.
RUN apt-get -yqq update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    wget ${SCALA_BINARY_DOWNLOAD_URL} && tar -zxvf ${SCALA_BINARY_ARCHIVE_NAME}.tgz -C /usr/local/ && \
    wget ${SBT_BINARY_DOWNLOAD_URL} && tar -zxvf ${SBT_BINARY_ARCHIVE_NAME}.tgz -C /usr/local/  && \
    wget ${SPARK_BINARY_DOWNLOAD_URL} && tar -zxvf ${SPARK_BINARY_ARCHIVE_NAME}.tgz -C /usr/local/ && \
    cd /usr/local/ && \
    ln -s sbt-launcher-packaging-${SBT_VERSION} sbt && \
    ln -s ${SCALA_BINARY_ARCHIVE_NAME} scala && \
    ln -s ${SPARK_BINARY_ARCHIVE_NAME} spark && \
    cp spark/conf/log4j.properties.template spark/conf/log4j.properties && \
    sed -i -e s/WARN/ERROR/g spark/conf/log4j.properties && \
    sed -i -e s/INFO/ERROR/g spark/conf/log4j.properties && \
    mkdir /root/.sbt
# We will be running our Spark jobs as `root` user.
USER root

# Working directory is set to the home folder of `root` user.
WORKDIR /root

# Expose ports for monitoring.
# SparkContext web UI on 4040 -- only available for the duration of the application.
# Spark master’s web UI on 8080.
# Spark worker web UI on 8081.
EXPOSE 4040 8080 8081
CMD ["/bin/bash"]
