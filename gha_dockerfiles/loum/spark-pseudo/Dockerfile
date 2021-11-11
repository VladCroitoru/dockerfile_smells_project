ARG SPARK_VERSION
ARG SPARK_RELEASE
ARG UBUNTU_BASE_IMAGE
ARG HADOOP_PSEUDO_BASE_IMAGE

FROM ubuntu:$UBUNTU_BASE_IMAGE AS downloader

ARG OPENJDK_8_HEADLESS
RUN apt-get update && apt-get install -y --no-install-recommends\
 wget\
 unzip\
 ca-certificates\
 git\
 openjdk-8-jdk-headless=$OPENJDK_8_HEADLESS

WORKDIR /tmp

ARG SPARK_VERSION
RUN git clone --depth 1 --branch v$SPARK_VERSION https://github.com/apache/spark.git

# Build a runnable distribution.
WORKDIR spark
ENV MAVEN_OPTS="-Xmx2g -XX:ReservedCodeCacheSize=2g"
ARG SPARK_RELEASE
RUN dev/make-distribution.sh\
 --name without-hadoop\
 --tgz\
 -Pyarn\
 -Phadoop-provided

### downloader stage end.

ARG HADOOP_PSEUDO_BASE_IMAGE
FROM loum/hadoop-pseudo:$HADOOP_PSEUDO_BASE_IMAGE

USER root

WORKDIR /opt

ARG SPARK_RELEASE
COPY --from=downloader /tmp/spark/$SPARK_RELEASE.tgz $SPARK_RELEASE.tgz
RUN tar zxf $SPARK_RELEASE.tgz\
 && ln -s $SPARK_RELEASE spark\
 && rm $SPARK_RELEASE.tgz

# Spark config.
ARG SPARK_HOME=/opt/spark
COPY files/spark-env.sh $SPARK_HOME/conf/spark-env.sh
COPY files/spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf

ARG SPARK_VERSION

COPY scripts/spark-bootstrap.sh /spark-bootstrap.sh

# YARN ResourceManager port.
EXPOSE 8032

# YARN ResourceManager webapp port.
EXPOSE 8088

# YARN NodeManager webapp port.
EXPOSE 8042

# Spark HistoryServer web UI port.
EXPOSE 18080

# Livy server port.
#EXPOSE 8998

# Start user run context.
USER hdfs
WORKDIR /home/hdfs

RUN sed -i "s|^export PATH=|export PATH=${SPARK_HOME}\/bin:|" ~/.bashrc

ENTRYPOINT [ "/spark-bootstrap.sh" ]
