FROM centos:7

MAINTAINER domeos

ENV KAFKA_VERSION 0.8.2.2
ENV SCALA_VERSION 2.11
ENV KAFKA_HOME /opt/kafka

ADD ./src /

RUN yum install -y java && yum clean all && \
    chmod +x /usr/local/sbin/start.sh && \
    curl -sS http://apache.fayea.com/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -o /opt/kafka.tar && \
    cd /opt && tar zxf kafka.tar && rm kafka.tar && \
    mv /opt/kafka_* /opt/kafka && \
    chown -R root:root /opt/kafka

RUN groupadd -r kafka && \
    useradd -c "Kafka" -d /var/lib/kafka -g kafka -M -r -s /sbin/nologin kafka && \
    mkdir /var/{lib,log}/kafka && \
    chown -R kafka:kafka /var/{lib,log}/kafka

EXPOSE 9092

VOLUME ["/var/lib/kafka"]

ENTRYPOINT ["/usr/local/sbin/start.sh"]

