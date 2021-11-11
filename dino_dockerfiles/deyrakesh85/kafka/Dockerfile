FROM deyrakesh85/ubuntu:jdk8

MAINTAINER Rakesh Dey <deyrakesh85@gmail.com>

RUN groupadd -r kafka && useradd -r -g kafka -s /bin/bash -m kafka

USER kafka

WORKDIR /home/kafka

RUN wget http://www-eu.apache.org/dist/kafka/1.0.1/kafka_2.11-1.0.1.tgz

RUN tar -zxvf kafka_2.11-1.0.1.tgz

RUN ln -s kafka_2.11-1.0.1 kafka

COPY configuration/server.properties /home/kafka/kafka/config

EXPOSE 9092

ENTRYPOINT ["/home/kafka/kafka/bin/kafka-server-start.sh", "kafka/config/server.properties"]
