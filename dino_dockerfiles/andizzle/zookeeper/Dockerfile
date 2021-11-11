FROM ubuntu:15.10

RUN apt-get update \
&& apt-get install -y openjdk-7-jre-headless wget iproute2 curl jq awscli \
&& apt-get clean

RUN wget -q -O - http://apache.mirrors.pair.com/zookeeper/zookeeper-3.5.1-alpha/zookeeper-3.5.1-alpha.tar.gz | tar -xzf - -C /opt \
&& mv /opt/zookeeper-3.5.1-alpha /opt/zookeeper

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

WORKDIR /opt/zookeeper

RUN cp ./conf/zoo_sample.cfg ./conf/zoo.cfg
RUN echo "standaloneEnabled=false" >> ./conf/zoo.cfg
RUN echo "dynamicConfigFile=/opt/zookeeper/conf/zoo.cfg.dynamic" >> ./conf/zoo.cfg

ADD aws-discover /usr/local/bin/
ADD zk-init /usr/local/bin/
