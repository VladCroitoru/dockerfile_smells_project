FROM hellgate75/apache-hadoop:2.8.0

MAINTAINER Fabrizio Torelli (hellgate75@gmail.com)

ENV SPARK_HOME=/usr/local/spark \
    HADOOP_CONF_DIR=/usr/local/spark/etc/hadoop \
    SPARK_VERSION=2.1.1 \
    APACHE_HADOOP_VERSION=2.7 \
    HADOOP_LIBEXEC_DIR=$HADOOP_HOME/libexec \
    SPARK_RUN_STANDALONE=true \
    SPARK_HADOOP_TGZ_URL="" \
    SPARK_CONFIG_TGZ_URL="" \
    SPARK_START_HADOOP=true \
    SPARK_START_HADOOP_ALL_SERVICES=false \
    SPARK_START_HADOOP_HDFS=true \
    SPARK_START_HADOOP_YARN=false \
    SPARK_START_HADOOP_JOB_HISTORY=false \
    SPARK_HADOOP_JOB_HISTORY_MAPRED_COMMAND="" \
    SPARK_START_HADOOP_DEAMONS=false \
    SPARK_START_HADOOP_DEAMON=false \
    SPARK_HADOOP_DEAMON_COMMAND="" \
    SPARK_START_HADOOP_YARN_DEAMONS=false \
    SPARK_START_HADOOP_YARN_DEAMON=false \
    SPARK_HADOOP_YARN_DEAMON_COMMAND="" \
    SPARK_START_HADOOP_BALANCER=false \
    SPARK_START_HADOOP_KMS_SERVER=false \
    SPARK_START_MASTER_NODE=true \
    SPARK_START_SLAVE_MASTER_HOST="" \
    SPARK_START_SLAVE_MASTER_PORT="" \
    SPARK_START_SLAVE_MASTER_WEBUI_PORT="" \
    SPARK_START_SLAVE_CORES=1 \
    SPARK_START_SLAVE_MEMORY=2g \
    SPARK_START_SLAVE_WORKER_DIR="/usr/local/spark/work" \
    SPARK_START_ALL_SERVICES=true \
    SPARK_START_ALL_SLAVES=false \
    SPARK_START_HISTORY_SERVER=false \
    SPARK_START_SHUFFLE_SERVICE=false \
    SPARK_START_DEAMONS=false \
    SPARK_START_DEAMON=false \
    SPARK_DAEMON_COMMAND="" \
    SPARK_START_THRIFT_SERVER=false \
    SPARK_START_MESOS_INTEGRATION=false \
    SPARK_START_INTEGRATE_WITH_YARN=false \
    SPARK_START_YARN_CLASSNAME="" \
    SPARK_START_YARN_ARGUMENTS="" \
    SPARK_START_YARN_QUEUE_NAME="master-queue" \
    SPARK_FORCE_HADOOP_RESTART=false \
    SPARK_FORCE_RESTART=false \
    SPARK_CONFIG_LOG_EVENT_ENABLED=true \
    SPARK_CONFIG_SERIALIZER_CLASS=org.apache.spark.serializer.KryoSerializer \
    SPARK_CONFIG_DRIVER_MEMORY=5g \
    SPARK_CONFIG_EXTRA_JVM_OPTIONS="" \
    SPARK_CONFIG_DEPLOY_RETAIN_APPS=200 \
    SPARK_CONFIG_DEPLOY_SPREADOUT=true \
    SPARK_CONFIG_RETAIN_DRIVERS=200 \
    SPARK_CONFIG_DEPLOY_DEFAULT_CORES=4 \
    SPARK_CONFIG_DEPLOY_MAX_EXEC_RETRIES=10 \
    SPARK_CONFIG_WORKER_TIMEOUT=60 \
    SPARK_CONFIG_WORKER_CLEANUP_ENABLED=false \
    SPARK_CONFIG_WORKER_CLEANUP_INTERVAL=1800 \
    SPARK_CONFIG_WORKER_CLEANUP_TTL=604800 \
    SPARK_CONFIG_WORKER_COMPRESSED_CACHE_SIZE=100 \
    SCALA_HOME=/usr/local/share/scala \
    PATH=$PATH:/usr/local/share/scala/bin:/usr/local/bin:/usr/local/spark/bin:/usr/local/spark/sbin


USER root

#support for Spark
RUN curl -s https://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_VERSION-bin-hadoop$APACHE_HADOOP_VERSION.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-$SPARK_VERSION-bin-hadoop$APACHE_HADOOP_VERSION spark

# define and update boot && docker run scripts
COPY bootstrap.sh /etc/bootstrap.sh
COPY docker-start-spark.sh /usr/local/bin/docker-start-spark
COPY spark-defaults-master.conf /usr/local/spark/conf/spark-defaults-master.conf
COPY spark-defaults-worker.conf /usr/local/spark/conf/spark-defaults-worker.conf
RUN chown root.root /etc/bootstrap.sh && \
    chown root.root /usr/local/bin/docker-start-spark && \
    chmod +x /etc/bootstrap.sh && \
    chmod +x /usr/local/bin/docker-start-spark && \
    mkdir -p $HADOOP_CONF_DIR && \
    mkdir -p /etc/config/spark && \
    mkdir -p /root/application

COPY sources.list /etc/apt/sources.backup.list
RUN cat /etc/apt/sources.list >> /etc/apt/sources.backup.list && \
    cat /etc/apt/sources.backup.list > /etc/apt/sources.list

#install R
RUN apt-get update && \
    apt-get -y --no-install-recommends install apt-transport-https && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/' && \
    apt-get update && \
    apt-get install -y r-base --no-install-recommends && \
    apt-get clean && \
    apt-get -y autoclean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root

#install Scala
RUN curl -LO http://www.scala-lang.org/files/archive/scala-2.12.2.deb && \
    sudo dpkg -i ./scala-2.12.2.deb
    # && \
    # echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list && \
    # apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \
    # apt-get update && \
    # apt-get install -y sbt --no-install-recommends && \
    # apt-get clean && \
    # apt-get -y autoclean && \
    # rm -rf /var/lib/apt/lists/*

WORKDIR $SPARK_HOME

CMD ["docker-start-spark", "-daemon"]

VOLUME ["/user/root/data/hadoop/hdfs/datanode", "/user/root/data/hadoop/hdfs/namenode", "/user/root/data/hadoop/hdfs/checkpoint", "/etc/config/hadoop", "/etc/config/spark", "mkdir -p /root/application"]

# Exposed Apache Haddop ports
# Apache Spark ports :
# 8080
# Apache Hadoop HDFS ports :
# 50010 50020 50070 50075 50090 8020 9000
# Apache Hadoop MAP Reduce ports :
# 10020 19888
# Apache Hadoop YARN ports:
# 8030 8031 8032 8033 8040 8042 8088
# Other Apache Hadoop ports:
# 49707 2122
EXPOSE 50010 50020 50070 50075 50090 8020 9000 10020 19888 8030 8031 8032 8033 8040 8042 8088 49707 2122 8080
