#
# Creates distributed hadoop-2.5.0 + oozie-4.0.1 + zookeeper-3.4.6 in ubuntu
# Based on sequenceiq/hadoop-docker (https://index.docker.io/u/sequenceiq/hadoop-docker/)
#
# VERSION 0.5

FROM ubuntu
MAINTAINER gappc <gapp.christian@gmail.com>

USER root

# Update system
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" >> /etc/apt/sources.list.d/webupd8team-java-precise.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" >> /etc/apt/sources.list.d/webupd8team-java-precise.list
RUN gpg --keyserver keyserver.ubuntu.com --recv C2518248EEA14886
RUN gpg --export --armor C2518248EEA14886 | sudo apt-key add -
RUN apt-get update

# Install java
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
RUN apt-get install -y oracle-java7-installer
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle
ENV PATH $PATH:$JAVA_HOME/bin
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> /root/.bashrc
RUN echo "export PATH=$PATH:$JAVA_HOME/bin" >> /root/.bashrc

# Install tools
RUN apt-get install -y curl openssh-server

# Install hadoop
RUN mkdir -p /opt/hadoop
RUN curl http://www.eu.apache.org/dist/hadoop/common/hadoop-2.5.0/hadoop-2.5.0.tar.gz --progress-bar | tar -xz -C /opt/hadoop/
RUN cd /opt/hadoop/ && ln -s hadoop-2.5.0 current
ENV HADOOP_PREFIX /opt/hadoop/current
ENV HADOOP_HOME /opt/hadoop/current

# Fixing the libhadoop.so
RUN rm  $HADOOP_HOME/lib/native/*
RUN curl -L http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-native-64-2.5.0.tar --progress-bar |tar -xz -C  $HADOOP_HOME/lib/native/

# Set hadoop configs
ADD hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh
ADD core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
ADD hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
ADD mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
ADD yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
ADD slaves $HADOOP_HOME/etc/hadoop/slaves

# Init hdfs
RUN $HADOOP_HOME/bin/hdfs namenode -format
RUN echo 1

# Copy oozie (COPYING FILES SHOULD BE AN EXCEPTION: since oozie must be build from sources, we copy the already build program from local directory to docker)
ADD oozie-4.0.1 /opt/oozie/oozie-4.0.1
RUN cd /opt/oozie/ && ln -s oozie-4.0.1 current
ENV OOZIE_HOME /opt/oozie/current

# Set oozie configs
ADD oozie-log4j.properties $OOZIE_HOME/conf/oozie-log4j.properties
ADD oozie-site.xml $OOZIE_HOME/conf/oozie-site.xml

# Install zookeeper
RUN mkdir -p /opt/zookeeper
RUN curl http://www.eu.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz --progress-bar | tar -xz -C /opt/zookeeper/
RUN cd /opt/zookeeper/ && ln -s zookeeper-3.4.6 current
ENV ZOOKEEPER_HOME /opt/zookeeper/current

# Set zookeeper config
ADD zoo.cfg $ZOOKEEPER_HOME/conf/zoo.cfg

# Configure passwordless ssh for Hadoop
RUN mkdir -p /root/.ssh
RUN mkdir -p /var/run/sshd
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

# Add public keys to authorized keys. Here you can add our own keys, if you don't want to type the password all the time
ADD gappc.pub /tmp/gappc.pub
RUN cat /tmp/gappc.pub >> /root/.ssh/authorized_keys

ADD sshd_config /etc/ssh/sshd_config
RUN echo LANG=”en_US.UTF-8” > /etc/default/locale

# Set commodity shell aliases
RUN echo "alias ls='ls --color=auto'" >> ~/.bashrc
RUN echo "alias ll='ls -alF'" >> ~/.bashrc
RUN echo "alias cdhadoop='cd /opt/hadoop/current'" >> ~/.bashrc
RUN echo "alias cdoozie='cd /opt/oozie/current'" >> ~/.bashrc
RUN echo "PATH=$ZOOKEEPER_HOME/bin:$OOZIE_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH" >> ~/.bashrc

# Set custom /etc/hosts file - needed for static ip and hostname resolution
ADD hosts /tmp/hosts

# Copy scripts
RUN echo 1
ADD docker-run.sh /sbin/docker-run.sh
RUN chmod u+x /sbin/docker-run.sh
ADD biohadoop-copy.sh /sbin/biohadoop-copy.sh
RUN chmod u+x /sbin/biohadoop-copy.sh

# Install pwgen to dynamically create root passwords on startup
RUN apt-get install -y pwgen

# Run standard command
CMD ["/sbin/docker-run.sh"]

EXPOSE 22 30000 54310 50020 50090 50070 22 50010 50075 8031 8032 8033 8040 8042 49707 8088 8030

