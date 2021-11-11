FROM alpine:3.2

MAINTAINER Micah Hausler <hausler.m@gmail.com>

# Install cURL
RUN apk --update add curl ca-certificates tar && \
    curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \
    apk add --allow-untrusted /tmp/glibc-2.21-r2.apk

# Java Version
ENV JAVA_VERSION_MAJOR 8
ENV JAVA_VERSION_MINOR 77
ENV JAVA_VERSION_BUILD 03
ENV JAVA_PACKAGE       jdk

# Download and unarchive Java
RUN mkdir /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"\
  http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
    | tar -xzf - -C /opt &&\
    ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk &&\
    rm -rf /opt/jdk/*src.zip \
           /opt/jdk/lib/missioncontrol \
           /opt/jdk/lib/visualvm \
           /opt/jdk/lib/*javafx* \
           /opt/jdk/jre/lib/plugin.jar \
           /opt/jdk/jre/lib/ext/jfxrt.jar \
           /opt/jdk/jre/bin/javaws \
           /opt/jdk/jre/lib/javaws.jar \
           /opt/jdk/jre/lib/desktop \
           /opt/jdk/jre/plugin \
           /opt/jdk/jre/lib/deploy* \
           /opt/jdk/jre/lib/*javafx* \
           /opt/jdk/jre/lib/*jfx* \
           /opt/jdk/jre/lib/amd64/libdecora_sse.so \
           /opt/jdk/jre/lib/amd64/libprism_*.so \
           /opt/jdk/jre/lib/amd64/libfxplugins.so \
           /opt/jdk/jre/lib/amd64/libglass.so \
           /opt/jdk/jre/lib/amd64/libgstreamer-lite.so \
           /opt/jdk/jre/lib/amd64/libjavafx*.so \
           /opt/jdk/jre/lib/amd64/libjfx*.so

# Set environment
ENV JAVA_HOME /opt/jdk
ENV PATH ${PATH}:${JAVA_HOME}/bin
#FROM java:openjdk-8-jre-alpine

ENV \
    ZK_RELEASE="http://www.apache.org/dist/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz" \
    EXHIBITOR_POM="https://raw.githubusercontent.com/Netflix/exhibitor/master/exhibitor-standalone/src/main/resources/buildscripts/standalone/maven/pom.xml"

ENV PATH $PATH:/usr/lib/mvn/bin

# Use one step so we can remove intermediate dependencies and minimize size
RUN \
    # Install dependencies
    apk update \
    && apk add wget bash curl \
    && wget --progress dot:mega http://ftp.fau.de/apache/maven/maven-3/3.3.1/binaries/apache-maven-3.3.1-bin.tar.gz \
    && tar xfz apache-maven-3.3.1-bin.tar.gz \
    && rm apache-maven-3.3.1-bin.tar.gz \
    && mv apache-maven-3.3.1 /usr/lib/mvn \

    # Install ZK
    && curl -s -Lo /tmp/zookeeper.tgz $ZK_RELEASE \
    && mkdir -p /opt/zookeeper/transactions /opt/zookeeper/snapshots \
    && tar xzf /tmp/zookeeper.tgz -C /opt/zookeeper --strip-components=1 \
    && rm /tmp/zookeeper.tgz \

    # Install Exhibitor
    && mkdir -p /opt/exhibitor \
    && curl -s -Lo /opt/exhibitor/pom.xml $EXHIBITOR_POM \
    && mvn -f /opt/exhibitor/pom.xml package \
    && ln -s /opt/exhibitor/target/exhibitor*jar /opt/exhibitor/exhibitor.jar

# Add the wrapper script to setup configs and exec exhibitor
ADD wrapper.sh /opt/exhibitor/wrapper.sh

# Add the optional web.xml for authentication
ADD web.xml /opt/exhibitor/web.xml

WORKDIR /opt/exhibitor
EXPOSE 2181 2888 3888 8080 8181

VOLUME /opt/zookeeper/local_configs

LABEL name="zookeeper" version="3.4.8"

ENTRYPOINT ["bash", "-ex", "/opt/exhibitor/wrapper.sh"]
