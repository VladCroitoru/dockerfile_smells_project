FROM jiridudekusy/docker-jdk8:centos

MAINTAINER Jiří Dudek <jiri.dudek@unicornsystems.eu>

ENV TOMCAT_MAJOR=8 \
    TOMCAT_VERSION=8.0.33 \
    TOMCAT_HOME=/opt/tomcat \
    CATALINA_HOME=/opt/tomcat \
    CATALINA_OUT=/dev/null

RUN curl -jksSL -o /tmp/apache-tomcat.tar.gz http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    gunzip /tmp/apache-tomcat.tar.gz && \
    tar -C /opt -xf /tmp/apache-tomcat.tar && \
    ln -s /opt/apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} && \
    rm -rf ${TOMCAT_HOME}/webapps/* && \
    rm -rf /tmp/* 

COPY logging.properties ${TOMCAT_HOME}/conf/logging.properties
COPY server.xml ${TOMCAT_HOME}/conf/server.xml

VOLUME ["/logs"]
EXPOSE 8080