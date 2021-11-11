FROM ubuntu:16.04
MAINTAINER adolphlwq kenan3015@gmail.com

# set time zone to shanghai
RUN ln -f -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#install java
RUN apt-get update && \
    apt-get install -y openssh-server openssh-client rsync openjdk-8-jre curl sudo

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    HADOOP_HOME=/usr/local/hadoop-2.6.4 \
    HADOOP_PREFIX=/usr/local/hadoop-2.6.4
ENV PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$PATH \
    HD_URL="http://ftp.tc.edu.tw/pub/Apache/hadoop/common/hadoop-2.6.4/hadoop-2.6.4.tar.gz"

#install hadoop
RUN curl -fL $HD_URL | tar xzf - -C /usr/local && \
    echo 'root:root' | chpasswd  && \
    sed -i "28s/.*/PermitRootLogin yes/g" /etc/ssh/sshd_config
#    echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config

ADD files/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
ADD files/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
ADD files/hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh
ADD entrypoint.sh /entrypoint.sh

# config ssh and init hadoop refer:https://github.com/sequenceiq/hadoop-docker/blob/master/Dockerfile#L17-L21
RUN chmod +x /entrypoint.sh && \
    #chown hadoop:hadoop -R $HADOOP_HOME && \
    chmod 755 -R $HADOOP_HOME && \
    apt-get remove -y curl && \
    apt-get clean && \
    rm -rf /etc/lib/apt/lists/* && \
    mkdir -p /hdfsdata/tmp && \
    mkdir -p /hdfsdata/namenode && \
    mkdir -p /hdfsdata/datanode1 && \
    chmod 755 -R /hdfsdata

#USER hadoop
CMD ["/entrypoint.sh", "-d"]
