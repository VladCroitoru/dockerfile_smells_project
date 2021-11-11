FROM ubuntu:15.10
MAINTAINER michael@faille.io

ENV WORKDIR /data

#ENV http_proxy http://172.17.42.1:3128
#ENV https_proxy $http_proxy

RUN apt-get update -y && \
    apt-get install wget -y && \
    wget http://archive.cloudera.com/cdh5/one-click-install/trusty/amd64/cdh5-repository_1.0_all.deb && \
    dpkg -i /cdh5-repository_1.0_all.deb && \
    apt-get update -y && \
    apt-get install -y  openjdk-8-jre-headless hadoop-hdfs-namenode hadoop-hdfs-datanode impala impala-server impala-shell impala-catalog impala-state-store -y && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data/persistent/dn



# Define working directory.
WORKDIR $WORKDIR


RUN mkdir /var/run/hdfs-sockets/
RUN chown hdfs.hadoop /var/run/hdfs-sockets/

RUN mkdir -p $WORKDIR/dn/
RUN chown hdfs.hadoop $WORKDIR/persistent/dn
RUN mkdir $WORKDIR/bin
ENV PATH=$PATH:$WORKDIR/bin
VOLUME $WORKDIR/persistent/dn


# Hadoop Configuration files
# /etc/hadoop/conf/ --> /etc/alternatives/hadoop-conf/ --> /etc/hadoop/conf/ --> /etc/hadoop/conf.empty/
# /etc/impala/conf/ --> /etc/impala/conf.dist
COPY etc/core-site.xml /etc/hadoop/conf/
COPY etc/hdfs-site.xml /etc/hadoop/conf/
COPY etc/core-site.xml /etc/impala/conf/
COPY etc/hdfs-site.xml /etc/impala/conf/
COPY etc/core-site.xml /etc/hive/conf/
COPY etc/hive-site.xml /etc/hive/conf/

# Various helper scripts
COPY bin/start.sh $WORKDIR/bin/
COPY bin/start-hdfs.sh $WORKDIR/bin/
COPY bin/start-impala.sh $WORKDIR/bin/
COPY bin/start-bash.sh $WORKDIR/bin/
COPY bin/start-daemon.sh $WORKDIR/bin/
RUN chmod +x $WORKDIR/bin/*
COPY bin/hdp /usr/bin/hdp

# HDFS PORTS :
# 9000  Name Node IPC
# 50010 Data Node Transfer
# 50020 Data Node IPC
# 50070 Name Node HTTP
# 50075 Data Node HTTP


# IMPALA PORTS :
# 21000 Impala Shell
# 21050 Impala ODBC/JDBC
# 25000 Impala Daemon HTTP
# 25010 Impala State Store HTTP
# 25020 Impala Catalog HTTP

EXPOSE 9000 50010 50020 50070 50075 21000 21050 25000 25010 25020



CMD $WORKDIR/bin/start-daemon.sh
