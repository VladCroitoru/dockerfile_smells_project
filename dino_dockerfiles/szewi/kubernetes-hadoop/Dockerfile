FROM ubuntu:16.04

LABEL maintainer="Kamil Szewczyk <szewinho@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:webupd8team/java 

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN apt-get update && apt-get install -y rsync openssh-server && \
  ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
  cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
  chmod 600 ~/.ssh/authorized_keys 

RUN cd /opt && wget -q http://www-eu.apache.org/dist/hadoop/common/hadoop-3.0.2/hadoop-3.0.2.tar.gz && \
  tar -xzf hadoop-3.0.2.tar.gz && rm -f hadoop-3.0.2.tar.gz && \
  ln -s hadoop-3.0.2 hadoop

ENV HADOOP_HOME="/opt/hadoop"
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV PATH=$PATH:$HADOOP_HOME/sbin
ENV HADOOP_MAPRED_HOME=${HADOOP_HOME}
ENV HADOOP_COMMON_HOME=${HADOOP_HOME}
ENV HADOOP_HDFS_HOME=${HADOOP_HOME}
ENV YARN_HOME=${HADOOP_HOME}

ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root

ENV HDFS_REPLICATION=1

RUN sed -i "s,^# export JAVA_HOME=,export JAVA_HOME=$JAVA_HOME,g" /opt/hadoop/etc/hadoop/hadoop-env.sh

ADD core-site.xml.template /opt/templates/
ADD hdfs-site.xml.template /opt/templates/

ADD bootstrap.sh /opt/bootstrap.sh
RUN chmod 700 /opt/bootstrap.sh

CMD ["/opt/bootstrap.sh", "-d"]
