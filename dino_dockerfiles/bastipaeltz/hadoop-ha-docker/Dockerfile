FROM williamyeh/java8

VOLUME /mnt/hadoop/

RUN apt-get update \
  && apt-get install -y jq curl \
  && curl -s http://www.eu.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz | tar -xz -C /usr/local/ \
  && cd /usr/local \
  && ln -s ./hadoop-2.7.3 hadoop \
  && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

ENV HADOOP_PREFIX /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_YARN_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop

WORKDIR /usr/local/hadoop

RUN sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/usr/lib/jvm/java-8-oracle\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_HOME=/usr/local/hadoop\n:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  \
  && sed -i '/^export HADOOP_CONF_DIR/ s:.*:export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:' $HADOOP_PREFIX/etc/hadoop/hadoop-env.sh \
  && chmod +x /usr/local/hadoop/etc/hadoop/*-env.sh

COPY core-site.xml.template hdfs-site.xml.template /usr/local/hadoop/etc/hadoop/

COPY bootstrap.sh fence.sh /etc/

CMD ["/etc/bootstrap.sh", "-d"]

# NameNode                Secondary NameNode  DataNode                     JournalNode  NFS Gateway    HttpFS         ZKFC
EXPOSE 8020 50070 50470   50090 50495         50010 1004 50075 1006 50020  8485 8480    2049 4242 111  14000 14001    8019
