FROM centos:6

MAINTAINER Ranjandas A P <thejranjan@gmail.com>

COPY files/etc/yum.repos.d/* /etc/yum.repos.d/
COPY files/etc/pki/rpm-gpg/* /etc/pki/rpm-gpg/

# Install JDK from Cloudera Manager repository
RUN yum install -y oracle-j2sdk1.7 && yum clean all

ENV JAVA_HOME=/usr/java/jdk1.7.0_67-cloudera/
ENV PATH=$PATH:$JAVA_HOME/bin

# Install hadoop package which contains pseudo-distributed configurations
RUN yum install -y hadoop-0.20-conf-pseudo hive-server sudo && yum clean all

COPY files/usr/local/libexec/init-hdfs.sh /usr/local/libexec/
RUN chmod +x /usr/local/libexec/init-hdfs.sh

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Ports list from http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/cdh_ig_ports_cdh5.html
# EXPOSE Hadoop HDFS Ports
EXPOSE 50010 50075 50475 50020 50070 8020 50090 8022

# Expose Hadoop MR Ports
EXPOSE 8021 8023 50030 50060

# Expose Hive Ports
EXPOSE 9083 10000 50111

CMD ["/usr/local/bin/entrypoint.sh"]
