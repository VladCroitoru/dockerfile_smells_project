FROM ubuntu:16.04
 
RUN apt-get update \
 && apt-get -y install wget tar openjdk-8-jdk dnsutils  net-tools\
 && apt-get clean

RUN cd /opt && \
    wget https://www-eu.apache.org/dist/zookeeper/stable/zookeeper-3.4.12.tar.gz && \
    tar xzvf /opt/zookeeper-3.4.12.tar.gz && \
    rm -rf /opt/zookeeper-3.4.12.tar.gz && \ 
    cd /opt/zookeeper-3.4.12

ENV ZK_HOME /opt/zookeeper-3.4.12

ADD zk-init.sh $ZK_HOME/bin/
RUN chmod 777 $ZK_HOME/bin/zk-init.sh

EXPOSE 2181 2888 3888
ENTRYPOINT ["$ZK_HOME/bin/zk-init.sh"]
