FROM alpine:3.3

RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk add --update openjdk8-jre curl bash procps openssh java-snappy@testing supervisor rsync libc6-compat
RUN mkdir -p ~root/.ssh /var/log/supervisor && chmod 700 ~root/.ssh/ && \
    echo -e "Port 22\n" >> /etc/ssh/sshd_config && \
    cp -a /etc/ssh /etc/ssh.cache && \
    rm -rf /var/cache/apk/*

RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.6.1-bin-hadoop2.6.tgz | tar -xz -C /usr/local && \
  cd /usr/local/ && \
  ln -s spark-1.6.1-bin-hadoop2.6 spark && \
  rm spark/lib/spark-examples-1.6.1-hadoop2.6.0.jar

ENV SPARK_HOME /usr/local/spark

RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa
RUN sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && sed -i "s/#AuthorizedKeysFile/AuthorizedKeysFile/g" /etc/ssh/sshd_config
RUN  echo -e "StrictHostKeyChecking no\n" >> /etc/ssh/ssh_config

RUN curl -s http://www-eu.apache.org/dist/hadoop/common/hadoop-2.6.4/hadoop-2.6.4.tar.gz | tar -xz -C /usr/local && \
  cd /usr/local/ && \
  ln -s hadoop-2.6.4 hadoop
  
ENV HADOOP_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop 
ENV HADOOP_LOG_DIR /usr/local/hadoop/logs
ENV JAVA_HOME /usr
ENV PATH $PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin

RUN mkdir -p /usr/local/hadoop/logs

WORKDIR /usr/local/spark