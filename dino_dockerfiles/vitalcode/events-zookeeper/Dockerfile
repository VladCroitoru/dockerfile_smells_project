FROM openjdk:8

MAINTAINER vitalcode

RUN apt-get update && \
    apt-get -y install jq

ENV ZK_VERSION=3.4.10

ENV ZK_FILE="zookeeper-${ZK_VERSION}"
ENV ZK_ARCHIVE_PATH="/tmp/${ZK_FILE}.tar.gz"
ENV ZK_HOME="/opt/zookeeper"

RUN APACHE_MIRROR=$(curl --stderr /dev/null https://www.apache.org/dyn/closer.cgi\?as_json\=1 | jq -r ".preferred") && \
    ZK_URL="${APACHE_MIRROR}/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz" && \
    wget "${ZK_URL}" -O ${ZK_ARCHIVE_PATH} && \
    tar xfz ${ZK_ARCHIVE_PATH} -C /opt && \
    ln -s /opt/${ZK_FILE} ${ZK_HOME}

RUN mv ${ZK_HOME}/conf/zoo_sample.cfg ${ZK_HOME}/conf/zoo.cfg

RUN sed -i "s|/tmp/zookeeper|$ZK_HOME/data|g" $ZK_HOME/conf/zoo.cfg; mkdir $ZK_HOME/data
RUN sed -i -r 's|#(log4j.appender.ROLLINGFILE.MaxBackupIndex.*)|\1|g' $ZK_HOME/conf/log4j.properties
RUN sed -i -r 's|#autopurge|autopurge|g' $ZK_HOME/conf/zoo.cfg

ADD start-zk.sh /usr/bin/
RUN chmod +x /usr/bin/start-zk.sh

EXPOSE 2181 2888 3888

CMD ["start-zk.sh"]
