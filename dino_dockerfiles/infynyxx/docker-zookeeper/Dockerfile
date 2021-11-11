FROM azul/zulu-openjdk:8

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install build-essential

RUN apt-get -y --force-yes --fix-missing install wget

ENV ZK_VER 3.4.10

RUN wget -q -O - http://mirror.vorboss.net/apache/zookeeper/zookeeper-$ZK_VER/zookeeper-$ZK_VER.tar.gz \
    | tar -xzf - -C /opt

ENV ZK_HOME /opt/zookeeper-$ZK_VER

RUN mkdir -p /data/zookeeper && mkdir -p /var/log/zookeeper

WORKDIR /opt/zookeeper-$ZK_VER

COPY *.cfg /opt/zookeeper-$ZK_VER/conf/

COPY *.properties /opt/zookeeper-$ZK_VER/conf/

ADD run.sh /opt/zookeeper-$ZK_VER/run.sh

EXPOSE 2181 2888 3888

RUN ls /opt/zookeeper-$ZK_VER/run.sh

CMD bash /opt/zookeeper-$ZK_VER/run.sh
