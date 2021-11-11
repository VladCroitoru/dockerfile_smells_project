FROM apache/zeppelin:0.7.3

MAINTAINER Saagie

# Install Spark 2.1.0 for Hadoop 2.6
RUN cd /tmp && wget https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.6.tgz -O /tmp/spark-2.1.0-bin-hadoop2.6.tgz

RUN cd /tmp && tar -xzf spark-2.1.0-bin-hadoop2.6.tgz && \
  cp spark-2.1.0-bin-hadoop2.6/conf/log4j.properties.template spark-2.1.0-bin-hadoop2.6/conf/log4j.properties && \
  mkdir -p /usr/local/spark/2.1.0 && mv spark-2.1.0-bin-hadoop2.6/* /usr/local/spark/2.1.0 && \
  rm -rf spark-2.1.0-bin-hadoop2.6.tgz spark-2.1.0-bin-hadoop2.6

# Install Mesos 1.3.1
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
  DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]') && \
  CODENAME=$(lsb_release -cs) && \
  echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | tee /etc/apt/sources.list.d/mesosphere.list && \
  apt-get -y update && \
  apt-get install -y --no-install-recommends mesos=1.3.1-2.0.1

# Install jq
RUN apt-get install -y jq

# Clean
RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/*

ENV MESOS_NATIVE_JAVA_LIBRARY /usr/lib/libmesos-1.3.1.so

# Set Spark 2.1.0 as the default one
ENV SPARK_HOME /usr/local/spark/2.1.0
ENV APACHE_SPARK_VERSION 2.1.0

# Set Hadoop default conf dir
ENV HADOOP_HOME /etc/hadoop
ENV HADOOP_CONF_DIR /etc/hadoop/conf

# Set Hive default conf dir
ENV ZEPPELIN_INTP_CLASSPATH_OVERRIDES /etc/hive/conf

# Default notebooks directory
ENV ZEPPELIN_NOTEBOOK_DIR '/notebook'

# Add a startup script that will setup Spark conf before running Zeppelin
ADD saagie-zeppelin.sh /zeppelin
ADD saagie-zeppelin-config.sh /zeppelin
RUN chmod 744 /zeppelin/saagie-zeppelin.sh /zeppelin/saagie-zeppelin-config.sh

# Set Saagie's cluster Java version
ENV JAVA_VERSION 8.131

# Install vim
RUN apt-get update
RUN apt-get -y install vim

# Add CRON to copy interpreter.json to persisted folder
RUN echo "* * * * * cp -f /zeppelin/conf/interpreter.json /notebook/" >> mycron && \
crontab mycron && \
rm mycron

# Keep default ENTRYPOINT as apache/zeppelin is using Tini, which is great.
CMD ["/zeppelin/saagie-zeppelin.sh"]
