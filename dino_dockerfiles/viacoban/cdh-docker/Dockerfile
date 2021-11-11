FROM centos:centos6
MAINTAINER Victor Iacoban <viacoban@adobe.com>

RUN yum -y install curl wget ntp tar

COPY cloudera-cdh4.repo /etc/yum.repos.d/
RUN rpm --import http://archive.cloudera.com/cdh4/redhat/6/x86_64/cdh/RPM-GPG-KEY-cloudera

COPY install-jdk.sh install-jdk.sh
RUN ["/bin/bash", "install-jdk.sh"]

ENV JAVA_HOME /usr/java/default
ENV PATH $JAVA_HOME/bin:$PATH

RUN yum -y install hadoop-0.20-mapreduce-jobtracker
RUN yum -y install hadoop-hdfs-namenode
RUN yum -y install hadoop-0.20-mapreduce-tasktracker hadoop-hdfs-datanode

RUN mkdir -p /cdh/bin
COPY start-all.sh /cdh/bin/
COPY hdfs-service.sh /cdh/bin/
COPY mapred-service.sh /cdh/bin/
COPY hbase-service.sh /cdh/bin/
ENV PATH $PATH:/cdh/bin

RUN ["/bin/bash", "hdfs-service.sh", "stop"]

COPY hadoop/conf/core-site.xml /etc/hadoop/conf/
COPY hadoop/conf/hdfs-site.xml /etc/hadoop/conf/
COPY hadoop/conf/mapred-site.xml /etc/hadoop/conf/

RUN mkdir -p /var/hdfs/data
RUN mkdir -p /var/hdfs/name
RUN hdfs namenode -format -nonInteractive -force
RUN chown -R hdfs:hdfs /var/hdfs/data
RUN chown -R hdfs:hdfs /var/hdfs/name

RUN ["/bin/bash", "hdfs-service.sh", "start"]

CMD ["/bin/bash", "start-all.sh"]

EXPOSE 2181 2888 3888
EXPOSE 8020 8021
EXPOSE 50010 50020 50030 50060 50070 50075
EXPOSE 60000 60010 60020 60030

