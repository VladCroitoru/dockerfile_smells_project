# DOCKER-VERSION 1.0.1
# VERSION        1.0

FROM debian:jessie
MAINTAINER Swaraj Yadav <yadav.swaraj@gmail.com>

RUN apt-get update && apt-get install -y openjdk-7-jre-headless wget vim net-tools
RUN wget -q -O - http://www.eu.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz | tar -xzf - -C /opt \
    && mv /opt/zookeeper-3.4.6 /opt/zookeeper \
    && mkdir -p /opt/zookeeper/data

COPY zoo.cfg /opt/zookeeper/conf/
COPY myid /opt/zookeeper/data/

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

EXPOSE 2181 2182 2183 2888 3887 3888 3889

WORKDIR /opt/zookeeper
