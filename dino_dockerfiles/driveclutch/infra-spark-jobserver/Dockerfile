FROM anapsix/alpine-java:jdk8

MAINTAINER Sang Venkatraman <sang@driveclutch.com>

USER root
WORKDIR /

RUN apk update && apk upgrade && \
apk add ca-certificates wget && update-ca-certificates && \
apk add curl git

ENV SBT_VERSION 0.13.11
ENV SCALA_VERSION 2.11.8
ENV SPARK_VERSION 1.6.2
ENV SPARK_JOBSERVER_BRANCH jobserver-0.7.0-SNAPSHOT-spark-1.6.2
ENV SPARK_VERSION_STRING spark-$SPARK_VERSION-bin-hadoop2.6
ENV SPARK_DOWNLOAD_URL http://d3kbcqa49mib13.cloudfront.net/$SPARK_VERSION_STRING.tgz

ENV SPARK_JOBSERVER_BUILD_HOME /spark-jobserver
ENV SPARK_JOBSERVER_APP_HOME /app
RUN mkdir -p $SPARK_JOBSERVER_APP_HOME

WORKDIR /opt

RUN wget --progress=bar https://github.com/DriveClutch/spark/releases/download/v1.6.2-scala2.11/spark-1.6.2-bin-hadoop-2.6.2-scala-2.11.tgz && \
tar zxvf spark-1.6.2-bin-hadoop-2.6.2-scala-2.11.tgz && \
mv spark-1.6.2-bin-hadoop-2.6.2-scala-2.11 spark && \
rm spark-1.6.2-bin-hadoop-2.6.2-scala-2.11.tgz

RUN wget http://dl.bintray.com/sbt/native-packages/sbt/0.13.11/sbt-0.13.11.tgz && \
tar zxvf sbt-0.13.11.tgz
ENV PATH="/opt/sbt/bin/:$PATH"

# Build Spark-Jobserver
#RUN git clone --branch $SPARK_JOBSERVER_BRANCH https://github.com/sangv/spark-jobserver.git
#WORKDIR $SPARK_JOBSERVER_BUILD_HOME
#RUN bin/server_deploy.sh docker && \
#    cd / && \
#    rm -rf -- $SPARK_JOBSERVER_BUILD_HOME

WORKDIR /opt
#RUN wget http://mirror.stjschools.org/public/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz && \
#tar zxvf apache-maven-3.3.9-bin.tar.gz
#RUN export PATH="/opt/apache-maven-3.3.9/bin:$PATH"

ENV JOBSERVER_MEMORY="2G"
RUN ["mkdir", "-p", "\/database"]
VOLUME ["\/database"]

RUN mkdir spark/app
WORKDIR spark
COPY app/spark-job-server.jar app/spark-job-server.jar
COPY app/server_start.sh app/server_start.sh
COPY app/server_stop.sh app/server_stop.sh
COPY app/manager_start.sh app/manager_start.sh
COPY app/setenv.sh app/setenv.sh
COPY app/log4j-stdout.properties app/log4j-server.properties
COPY app/docker.conf app/docker.conf
COPY app/docker.sh app/settings.sh

COPY lib/datanucleus-api-jdo-3.2.6.jar /opt/spark/lib/datanucleus-api-jdo-3.2.6.jar
COPY lib/datanucleus-core-3.2.10.jar /opt/spark/lib/datanucleus-core-3.2.10.jar
COPY lib/datanucleus-rdbms-3.2.9.jar /opt/spark/lib/datanucleus-rdbms-3.2.9.jar

ENV SPARK_HOME="/opt/spark"

ENTRYPOINT ["/opt/spark/app/server_start.sh"]
