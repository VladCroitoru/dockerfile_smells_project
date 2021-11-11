FROM sequenceiq/hadoop-docker:2.7.1

MAINTAINER Jiayu Liu <etareduce@gmail.com>

ENV HIVE_HOME=/usr/lib/hive \
    HADOOP_HOME=/usr/local/hadoop \
    HIVE_VERSION=2.1.1 \
    MYSQL_VERSION=5.1.40

ENV HIVE_CONF $HIVE_HOME/conf \
    HIVE_LIB $HIVE_HOME/lib \
    HADOOP_COMMON_HOME=$HADOOP_HOME/share/hadoop/common \
    HADOOP_HDFS_HOME=$HADOOP_HOME/share/hadoop/hdfs \
    HADOOP_MAPRED_HOME=$HADOOP_HOME/share/hadoop/mapreduce \
    HADOOP_YARN_HOME=$HADOOP_HOME/share/hadoop/yarn

RUN mkdir -p $HIVE_HOME \
    && curl -Lo /tmp/apache-hive-$HIVE_VERSION-bin.tar.gz https://mirrors.tuna.tsinghua.edu.cn/apache/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz \
    && tar -xvf /tmp/apache-hive-$HIVE_VERSION-bin.tar.gz -C $HIVE_HOME --strip-components=1 \
    && rm /tmp/apache-hive-$HIVE_VERSION-bin.tar.gz \
    && curl -Lo /tmp/mysql-connector-java-$MYSQL_VERSION.tar.gz https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-$MYSQL_VERSION.tar.gz \
    && tar -xvf /tmp/mysql-connector-java-$MYSQL_VERSION.tar.gz -C /tmp \
    && mv /tmp/mysql-connector-java-$MYSQL_VERSION/mysql-connector-java-$MYSQL_VERSION-bin.jar $HIVE_LIB/ \
    && rm -r /tmp/mysql-connector-java-$MYSQL_VERSION /tmp/mysql-connector-java-$MYSQL_VERSION.tar.gz

ENV PATH $HIVE_HOME/bin:$PATH

# add the jdbc driver for metastore
ADD hive-site.xml $HIVE_CONF/hive-site.xml
ADD entrypoint.sh $HIVE_HOME/entrypoint.sh

WORKDIR $HIVE_HOME

EXPOSE 10000 9083 9000

ENTRYPOINT "./entrypoint.sh"
