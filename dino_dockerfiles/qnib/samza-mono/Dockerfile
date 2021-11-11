# Fully fletched samza image
FROM qnib/java7

RUN useradd hadoop
ENV HADOOP_VER=2.5.2 \
    SCALA_VER=2.10.4 \
    SAMZA_BASE_VER=2.10 \
    SLF4J_VER=1.0.1 \
    SAMZA_VER=0.8.0 \
    HDFS_LIB_DIR=/opt/hadoop/share/hadoop/hdfs/lib \
    HDFS_URL=http://search.maven.org/remotecontent

RUN curl -fsL http://apache.claz.org/hadoop/common/hadoop-${HADOOP_VER}/hadoop-${HADOOP_VER}.tar.gz | tar xzf - -C /opt && mv /opt/hadoop-${HADOOP_VER} /opt/hadoop
ADD opt/hadoop/etc/hadoop/* /opt/hadoop/etc/hadoop/
## Install SSH
RUN yum install -y openssh-server
ADD etc/consul.d/check_sshd.json /etc/consul.d/
ADD opt/qnib/bin/startup_sshd.sh /opt/qnib/bin/
ADD etc/bashrc.hadoop /etc/bashrc.hadoop
RUN echo "source /etc/bashrc.hadoop" >> /etc/bashrc

VOLUME ["/data/hadoopdata/hdfs"]
ADD opt/qnib/hadoop/bin/ /opt/qnib/hadoop/bin/
ADD etc/supervisord.d/hdfs.ini \
    etc/supervisord.d/sshd.ini \
    etc/supervisord.d/yarn.ini \
    /etc/supervisord.d/
ADD etc/consul.d/check_hdfs.json \
    etc/consul.d/check_sshd.json \
    etc/consul.d/check_yarn.json \
    /etc/consul.d/


RUN yum install -y bsdtar maven
RUN mkdir -p ${HADOOP_YARN_HOME}/share/hadoop/hdfs/lib && \
    curl -fsL http://www.scala-lang.org/files/archive/scala-${SCALA_VER}.tgz |tar xzf - -C /opt/ && \
    cp /opt/scala-${SCALA_VER}/lib/{scala-compiler.jar,scala-library.jar} /opt/hadoop/share/hadoop/hdfs/lib/ && \
    rm -rf /opt/scala-${SCALA_VER}
RUN curl -sLo ${HDFS_LIB_DIR}/grizzled-slf4j_${SAMZA_BASE_VER}-${SLF4J_VER}.jar ${HDFS_URL}?filepath=org/clapper/grizzled-slf4j_${SAMZA_BASE_VER}/${SLF4J_VER}/grizzled-slf4j_${SAMZA_BASE_VER}-${SLF4J_VER}.jar && \
    curl -sLo ${HDFS_LIB_DIR}/samza-yarn_${SAMZA_BASE_VER}-${SAMZA_VER}.jar ${HDFS_URL}?filepath=org/apache/samza/samza-yarn_${SAMZA_BASE_VER}/${SAMZA_VER}/samza-yarn_${SAMZA_BASE_VER}-${SAMZA_VER}.jar && \
    curl -sLo ${HDFS_LIB_DIR}/samza-core_${SAMZA_BASE_VER}-${SAMZA_VER}.jar ${HDFS_URL}?filepath=org/apache/samza/samza-core_${SAMZA_BASE_VER}/${SAMZA_VER}/samza-core_${SAMZA_BASE_VER}-${SAMZA_VER}.jar
ADD opt/hadoop/etc/hadoop/core-site.xml /opt/hadoop/etc/hadoop/

### Zookeeper
VOLUME ["/tmp/zookeeper"]
ENV ZK_VER 3.4.6
RUN curl -fsL http://apache.mirror.digitalpacific.com.au/zookeeper/zookeeper-${ZK_VER}/zookeeper-${ZK_VER}.tar.gz | tar xzf - -C /opt && mv /opt/zookeeper-${ZK_VER} /opt/zookeeper
RUN yum install -y bc jq
ADD etc/supervisord.d/zookeeper*.ini /etc/supervisord.d/
ADD opt/qnib/zookeeper/bin/*.sh /opt/qnib/zookeeper/bin/
ADD etc/consul.d/zookeeper.json /etc/consul.d/
ADD opt/zookeeper/conf/zoo.cfg /opt/zookeeper/conf/
ADD etc/consul-templates/zoo.cfg.ctmpl etc/consul-templates/zoo.myid.ctmpl /etc/consul-templates/
ENV PATH=/opt/zookeeper/bin:${PATH}
RUN echo "tail -f /var/log/supervisor/zookeeper.log" >> /root/.bash_history && \
    echo "cat /opt/zookeeper/conf/zoo.cfg" >> /root/.bash_history

### Kafka
ENV KAFKA_VER=0.8.2.1 \
    API_VER=2.11
RUN curl -fLs http://apache.mirrors.pair.com/kafka/${KAFKA_VER}/kafka_${API_VER}-${KAFKA_VER}.tgz | tar xzf - -C /opt && mv /opt/kafka_${API_VER}-${KAFKA_VER} /opt/kafka/
ADD etc/supervisord.d/kafka*.ini /etc/supervisord.d/
ADD opt/kafka/config/server.properties /opt/kafka/config/
ADD opt/qnib/kafka/bin/*.sh /opt/qnib/kafka/bin/
ADD etc/consul.d/kafka.json /etc/consul.d/
ADD etc/consul-templates/kafka.server.properties.ctmpl /etc/consul-templates/
RUN echo "/opt/kafka/bin/kafka-console-consumer.sh --zookeeper zookeeper.service.consul:2181 --topic syslog" >> /root/.bash_history && \
    echo "/opt/kafka/bin/kafka-topics.sh --zookeeper zookeeper.service.consul:2181 --replication-factor 3 --partitions 1 --create --topic ring0" >> /root/.bash_history && \
    echo "/opt/kafka/bin/kafka-run-class.sh kafka.admin.TopicCommand --zookeeper zookeeper.service.consul:2181 --topic ring0 --describe" >> /root/.bash_history && \
    echo "/opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic ring0" >> /root/.bash_history && \
    echo "/opt/kafka/bin/kafka-topics.sh --zookeeper zookeeper.service.consul:2181 --describe --topic \$(/opt/kafka/bin/kafka-topics.sh --zookeeper zookeeper.service.consul:2181 --list|xargs|sed -e 's/ /,/g')" >> /root/.bash_history

## Temporarily until moved to qnib/consul
ADD opt/qnib/consul/etc/bash_functions /opt/qnib/consul/etc/
ADD opt/qnib/kafka/bin/show_topics.py /opt/qnib/kafka/bin/

## Samza
RUN yum install -y git-core
RUN git clone http://git-wip-us.apache.org/repos/asf/samza.git /opt/samza && \
    cd /opt/samza && \
    ./gradlew  publishToMavenLocal

## Hello Samza
RUN chown hadoop: /opt/
USER hadoop
## passwordless login for hadoop user
RUN ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa && \
    cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys
ADD ssh/config /home/hadoop/.ssh/config
RUN curl -sfL https://github.com/apache/samza-hello-samza/archive/master.zip |bsdtar xf - -C /opt/ && \
    mv /opt/samza-hello-samza-master /opt/hello-samza/ && \
    cd /opt/hello-samza && \
    mvn clean package
RUN mkdir -p /opt/hello-samza/deploy/samza/ && \
    tar xzf /opt/hello-samza/target/hello-samza-0.10.0-dist.tar.gz -C /opt/hello-samza/deploy/samza/
USER root
