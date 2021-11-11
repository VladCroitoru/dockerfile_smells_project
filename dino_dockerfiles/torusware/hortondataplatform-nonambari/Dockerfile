FROM centos:centos6
MAINTAINER Oscar García <oscar.garcia@torusware.com>

WORKDIR /root
COPY scripts /root/scripts

# Required packages download and installation:
RUN yum -y update; \
    yum install -y htop openssh-server openssh-clients wget mysql-server \
        mysql-connector-java; \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key; \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key; \
    ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa; \
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys; \
    service sshd start; chkconfig sshd on; \
    wget http://www-lry.ciril.net/client/java/jdk-7u75-linux-x64.rpm ; \
    rpm -Uh jdk-7u75-linux-x64.rpm; rm -rf jdk-7u75-linux-x64.rpm; \
    wget -nv http://public-repo-1.hortonworks.com/HDP/centos6/2.x/updates/2.3.4.0/hdp.repo \
        -O /etc/yum.repos.d/hdp.repo; \
    yum repolist; \
    yum install -y hadoop hadoop-hdfs hadoop-libhdfs hive hive-metastore \
        hadoop-yarn hadoop-mapreduce hadoop-client hbase spark snappy snappy-devel; \
    yum install -y ntp; \
    yum clean all

ENV SPARK_HOME /usr/hdp/current/spark-client
ENV HADOOP_CONF_DIR /etc/hadoop/conf
ENV HADOOP_HOME /usr/hdp/current/hadoop-client
ENV HADOOP_PREFIX /usr/hdp/current/hadoop-client
ENV HIVE_CONF_DIR /etc/hive/conf

CMD ["/root/scripts/entrypoint.sh"]
