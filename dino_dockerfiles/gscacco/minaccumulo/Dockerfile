# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
FROM phusion/baseimage:0.9.4

EXPOSE 50070 50095 2181 9997 9000

# Use baseimage-docker's init system.
RUN rm -f /etc/service/sshd/down
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
CMD ["/sbin/my_init"]

RUN apt-get update
RUN apt-get install -y openjdk-7-jdk wget

# Environment variables
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/
ENV HADOOP_HOME /root/installs/hadoop-2.6.3
ENV ZOOKEEPER_HOME /root/installs/zookeeper-3.4.6

#Change this setting for performances
RUN sed -i 's/securerandom.source=file:\/dev\/urandom/securerandom.source=file:\/dev\/\.\/urandom/' $JAVA_HOME/jre/lib/security/java.security

RUN ssh-keygen -f ~/.ssh/id_rsa -P ''
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN echo "Host *" >> /etc/ssh/ssh_config && echo "   StrictHostKeyChecking no" >> /etc/ssh/ssh_config && echo "   UserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config
RUN mkdir -p /root/downloads
WORKDIR /root/downloads
RUN wget http://it.apache.contactlab.it/hadoop/common/hadoop-2.6.3/hadoop-2.6.3.tar.gz
RUN wget http://apache.panu.it/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
RUN wget https://archive.apache.org/dist/accumulo/1.6.4/accumulo-1.6.4-bin.tar.gz
RUN mkdir -p /root/installs
WORKDIR /root/installs
RUN tar zxvf /root/downloads/hadoop-2.6.3.tar.gz
RUN tar zxvf /root/downloads/zookeeper-3.4.6.tar.gz
RUN tar zxvf /root/downloads/accumulo-1.6.4-bin.tar.gz

RUN sed -i 's/<configuration>/<configuration>\n\t<property>\n\t\t<name>fs.defaultFS<\/name>\n\t\t<value>hdfs:\/\/localhost:9000<\/value>\n\t<\/property>/' hadoop-2.6.3/etc/hadoop/core-site.xml

RUN sed -i 's/<configuration>/\
<configuration>\n\
    <property>\n\
        <name>dfs.replication<\/name>\n\
        <value>1<\/value>\n\
    <\/property>\n\
    <property>\n\
        <name>dfs.name.dir<\/name>\n\
        <value>hdfs_storage\/name<\/value>\n\
    <\/property>\n\
    <property>\n\
        <name>dfs.data.dir<\/name>\n\
        <value>hdfs_storage\/data<\/value>\n\
    <\/property>\n\
/' hadoop-2.6.3/etc/hadoop/hdfs-site.xml

RUN printf '\
<?xml version="1.0"?>\n\
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\
<configuration>\n\
     <property>\n\
         <name>mapred.job.tracker</name>\n\
         <value>localhost:9001</value>\n\
     </property>\n\
</configuration>\n\
' >> hadoop-2.6.3/etc/hadoop/mapred-site.xml

RUN sed -i 's/export JAVA_HOME=${JAVA_HOME}/export JAVA_HOME=\/usr\/lib\/jvm\/java-7-openjdk-amd64/' hadoop-2.6.3/etc/hadoop/hadoop-env.sh

WORKDIR /root/installs/hadoop-2.6.3

RUN cp ~/installs/zookeeper-3.4.6/conf/zoo_sample.cfg ~/installs/zookeeper-3.4.6/conf/zoo.cfg

RUN cp ~/installs/accumulo-1.6.4/conf/examples/512MB/native-standalone/* ~/installs/accumulo-1.6.4/conf/
RUN sed -i 's/# export ACCUMULO_MONITOR_BIND_ALL="true"/export ACCUMULO_MONITOR_BIND_ALL="true"/' ~/installs/accumulo-1.6.4/conf/accumulo-env.sh

RUN sed -i 's/ACCUMULO_TSERVER_OPTS="${POLICY} -Xmx48m -Xms48m "/ACCUMULO_TSERVER_OPTS="${POLICY} -Xmx1536m -Xms1536m "/' ~/installs/accumulo-1.6.4/conf/accumulo-env.sh
RUN sed -i 's/ACCUMULO_MASTER_OPTS="${POLICY} -Xmx128m -Xms128m"/ACCUMULO_MASTER_OPTS="${POLICY} -Xmx1024m -Xms1024m"/' ~/installs/accumulo-1.6.4/conf/accumulo-env.sh
RUN sed -i 's/ACCUMULO_MONITOR_OPTS="${POLICY} -Xmx64m -Xms64m"/ACCUMULO_MONITOR_OPTS="${POLICY} -Xmx1024m -Xms1024m"/' ~/installs/accumulo-1.6.4/conf/accumulo-env.sh
RUN sed -i 's/ACCUMULO_GC_OPTS="-Xmx64m -Xms64m"/ACCUMULO_GC_OPTS="-Xmx256m -Xms256m"/' ~/installs/accumulo-1.6.4/conf/accumulo-env.sh
RUN sed -i 's/ACCUMULO_OTHER_OPTS="-Xmx128m -Xms64m"/ACCUMULO_OTHER_OPTS="-Xmx1024m -Xms1024m"/' ~/installs/accumulo-1.6.4/conf/accumulo-env.sh

RUN sed -i 's/<value>DEFAULT<\/value>/<value>password<\/value>/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml
RUN sed -i 's/<value>secret<\/value>/<value>password<\/value>/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml
RUN sed -i 's/<\/configuration>/\
<property>\n\
    <name>instance.volumes<\/name>\n\
    <value>hdfs:\/\/localhost:9000\/accumulo<\/value>\n\
<\/property>\n\
<\/configuration>\n\
/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml

RUN sed -i 's/80M/1G/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml
RUN sed -i 's/7M/128M/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml
RUN sed -i 's/20M/256M/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml
RUN sed -i 's/50M/200M/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml
RUN sed -i 's/100M/1G/' ~/installs/accumulo-1.6.4/conf/accumulo-site.xml

ADD sshd_start.sh /etc/my_init.d/01_sshd_start.sh
ADD hadoop_format_hdfs.sh /etc/my_init.d/02_hadoop_format_hdfs.sh
ADD hadoop_start.sh /etc/my_init.d/03_hadoop_start.sh
ADD zookeeper_start.sh /etc/my_init.d/04_zookeeper_start.sh
ADD accumulo_init.sh /etc/my_init.d/05_accumulo_init.sh
ADD accumulo_start.sh /etc/my_init.d/06_accumulo_start.sh

RUN rm -f /root/downloads/*
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
