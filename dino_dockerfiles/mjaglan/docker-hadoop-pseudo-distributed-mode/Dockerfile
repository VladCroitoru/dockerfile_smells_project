# author mjaglan@umail.iu.edu
# Coding Style: Shell form

# Start from Ubuntu OS image
FROM ubuntu:14.04

# set root user
USER root

# install utilities on up-to-date node
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y openssh-server default-jdk wget

# set java home
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64

# setup ssh with no passphrase
RUN ssh-keygen -t rsa -f $HOME/.ssh/id_rsa -P "" \
    && cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys

# download & extract & move hadoop & clean up
# TODO: write a way of untarring file to "/usr/local/hadoop" directly
RUN wget -O /hadoop.tar.gz -q https://iu.box.com/shared/static/u9wy21nev5hxznhuhu0v6dzmcqhkhaz7.gz \
	&& tar xfz hadoop.tar.gz \
	&& mv /hadoop-2.7.3 /usr/local/hadoop \
	&& rm /hadoop.tar.gz

# hadoop environment variables
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin 

# hadoop-store
RUN mkdir -p $HADOOP_HOME/hdfs/namenode \
	&& mkdir -p $HADOOP_HOME/hdfs/datanode

# setup configs - [standalone, pseudo-distributed mode, fully distributed mode]
# NOTE: Directly using COPY/ ADD will NOT work if you are NOT using absolute paths inside the docker image.
# Temporary files: http://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s18.html
COPY config/ /tmp/
RUN mv /tmp/ssh_config $HOME/.ssh/config \
    && mv /tmp/hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh \
    && mv /tmp/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml \
    && mv /tmp/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml \
    && mv /tmp/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml.template \
    && cp $HADOOP_HOME/etc/hadoop/mapred-site.xml.template $HADOOP_HOME/etc/hadoop/mapred-site.xml \
    && mv /tmp/yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml

# Add startup script
ADD scripts/hadoop-services.sh $HADOOP_HOME/hadoop-services.sh

# set permissions
RUN chmod 744 -R $HADOOP_HOME

# format namenode
RUN $HADOOP_HOME/bin/hdfs namenode -format

# run hadoop services
ENTRYPOINT $HADOOP_HOME/hadoop-services.sh; bash

