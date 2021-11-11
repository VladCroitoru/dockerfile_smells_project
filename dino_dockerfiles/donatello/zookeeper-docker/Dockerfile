FROM debian:jessie
MAINTAINER Aditya Manthramurthy

RUN apt-get -q update && apt-get install -qy openjdk-7-jre-headless wget python

RUN wget -q -O - http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz | tar -xzf - -C /opt \
    && mv /opt/zookeeper-3.4.6 /opt/zookeeper \
    && cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

EXPOSE 2181 2888 3888

WORKDIR /opt/zookeeper

VOLUME ["/var/lib/zookeeper", "/var/log/zookeeper"]

ADD run.py /opt/zookeeper/.docker/run.py
RUN chmod +x /opt/zookeeper/.docker/run.py

ENTRYPOINT ["/opt/zookeeper/.docker/run.py"]
