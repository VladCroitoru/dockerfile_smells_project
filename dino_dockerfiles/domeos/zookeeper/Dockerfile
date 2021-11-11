FROM centos:7

MAINTAINER domeos

ENV ZOOKEEPER_VERSION 3.4.6

ADD ./src /

RUN yum install -y java && yum clean all && \
    chmod +x /usr/local/sbin/start.sh && \
    curl -sS http://mirrors.sonic.net/apache/zookeeper/current/zookeeper-${ZOOKEEPER_VERSION}.tar.gz -o /opt/zookeeper.tar.gz && \
    cd /opt && \
    tar zxvf zookeeper.tar.gz && \
    rm zookeeper.tar.gz &&\
    mv /opt/zookeeper-* /opt/zookeeper && \
    chown -R root:root /opt/zookeeper

RUN groupadd -r zookeeper && \
    useradd -c "Zookeeper" -d /var/lib/zookeeper -g zookeeper -M -r -s /sbin/nologin zookeeper && \
    mkdir /var/lib/zookeeper && \
    chown -R zookeeper:zookeeper /var/lib/zookeeper

EXPOSE 2181 2888 3888

VOLUME ["/opt/zookeeper/conf", "/var/lib/zookeeper"]

ENTRYPOINT ["/usr/local/sbin/start.sh"]

