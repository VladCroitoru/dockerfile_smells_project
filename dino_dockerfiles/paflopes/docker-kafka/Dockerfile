FROM quay.io/ukhomeofficedigital/centos-base:v0.2.0

RUN yum upgrade -y -q; yum clean all
RUN yum install -y -q java-headless tar wget; yum clean all

EXPOSE 9092

ENV KAFKA_VERSION 0.9.0.1
ENV SCALA_VERSION 2.11
RUN wget -q http://mirror.vorboss.net/apache/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -O - | tar -xzf -; mv kafka_${SCALA_VERSION}-${KAFKA_VERSION} /kafka

VOLUME /data
WORKDIR /kafka
COPY config/server.properties /kafka/config/server.properties
COPY run.sh /run.sh

CMD /run.sh
