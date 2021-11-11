FROM ubuntu:14.04

MAINTAINER Todd Morrison <todd@deepelement.com>

RUN apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-properties-common python-software-properties
RUN apt-add-repository -y ppa:webupd8team/java
RUN apt-get -y update
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java7-installer oracle-java7-set-default

RUN apt-get -y install curl
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-{SPARK_VERSION}-bin-hadoop{HADOOP_VERSION}.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-{SPARK_VERSION}-bin-hadoop{HADOOP_VERSION} spark
ENV SPARK_HOME="/usr/local/spark-{SPARK_VERSION}-bin-hadoop{HADOOP_VERSION}"

# Deploy Script
ADD scripts/start-master.sh $SPARK_HOME/start-master.sh
ADD scripts/start-worker.sh $SPARK_HOME/start-worker.sh
ADD scripts/spark-shell.sh  $SPARK_HOME/spark-shell.sh
ADD scripts/remove_alias.sh $SPARK_HOME/remove_alias.sh

# Deploy Config
ADD scripts/spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf

ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002 -Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 -Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040 -Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"
ENV SPARK_WORKER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002 -Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004 -Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040 -Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_WORKER_PORT 8888
ENV SPARK_WORKER_WEBUI_PORT 8081

EXPOSE 8080 7077 8888 8081 4040 7001 7002 7003 7004 7005 7006

RUN ln -s $SPARK_HOME /SPARK_HOME