FROM pavlovmedia/docker-java8
MAINTAINER Shawn Dempsay <sdempsay@pavlovmedia.com>

ENV AMQ_VER=5.14.1

ADD http://www.mirrorservice.org/sites/ftp.apache.org/activemq/${AMQ_VER}/apache-activemq-${AMQ_VER}-bin.tar.gz /tmp

RUN mkdir -p /opt/amq && \
    cd /opt/amq && \
    tar xvzf /tmp/apache-activemq-${AMQ_VER}-bin.tar.gz && \
    ln -s /opt/amq/apache-activemq-${AMQ_VER} /opt/amq/current

# TODO: Copy config file
EXPOSE 61616 61613 1883

ENV JVM_OPTIONS="-Dactivemq.home=/opt/amq/current"

WORKDIR /opt/amq/current
CMD exec java $JVM_OPTIONS -jar bin/activemq.jar start
