FROM debian:jessie

# install base system
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y apt-utils apt-transport-https

# install dev environment
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list
RUN apt-get update
RUN apt-get install -y sudo vim krb5-user git wget
RUN apt-get -t jessie-backports install -y openjdk-8-jdk-headless

# install CDH5
RUN echo "deb http://archive.cloudera.com/cdh5/debian/jessie/amd64/cdh jessie-cdh5 contrib" > /etc/apt/sources.list.d/cloudera.list
ADD https://archive.cloudera.com/cdh5/debian/jessie/amd64/cdh/archive.key /tmp/cloudera-archive.key
RUN apt-key add /tmp/cloudera-archive.key

COPY cloudera.pref /etc/apt/preferences.d/cloudera.pref

RUN apt-get update
RUN apt-get install -y hadoop-conf-pseudo

#RUN perl -pi -e 's|</configuration>|  <property><name>yarn.nodemanager.disk-health-checker.enable</name><value>false</value></property>\n</configuration>|' /etc/hadoop/conf/yarn-site.xml

RUN sudo -u hdfs hdfs namenode -format

RUN service hadoop-hdfs-datanode start && \
    service hadoop-hdfs-namenode start && \
    service hadoop-hdfs-secondarynamenode start && \
    /usr/lib/hadoop/libexec/init-hdfs.sh && \
    sudo -u hdfs hadoop fs -ls -R / && \
    service hadoop-hdfs-datanode stop && \
    service hadoop-hdfs-namenode stop && \
    service hadoop-hdfs-secondarynamenode stop

#
# Install hive
#
RUN apt-get update
RUN apt-get install -y hive hive-server2

# use our config
COPY hive-site.xml /etc/alternatives/hive-conf/hive-site.xml

# some user env stuff
RUN echo "alias ls='ls -F'">~/.bashrc

RUN useradd joe -m -s /bin/bash
RUN echo "export HADOOP_MAPRED_HOME=/usr/lib/hadoop-mapreduce">>/root/.bashrc
RUN echo "alias ls='ls -F'">>/root/.bashrc

WORKDIR /

# needed for adding data to our hive install (added during bootstrap)
COPY dvdstore /root/

# and let's bootstrap!
COPY bootstrap.sh /usr/local/bin/bootstrap.sh
RUN chmod 755 /usr/local/bin/bootstrap.sh
CMD ["/usr/local/bin/bootstrap.sh"]
