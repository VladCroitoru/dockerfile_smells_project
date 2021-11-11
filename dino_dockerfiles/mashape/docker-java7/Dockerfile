# java
#
# VERSION       Java 7

# use the centos base image provided by dotCloud
FROM centos:7
MAINTAINER Marco Palladino, marco@mashape.com

ENV JAVA_VERSION 7u75
ENV BUILD_VERSION b13

# Upgrading system
RUN yum -y upgrade && \
    curl -L -k  -H "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" > /tmp/jdk-7-linux-x64.rpm && \
    yum -y install /tmp/jdk-7-linux-x64.rpm && \
    yum clean all && rm -rf /tmp/jdk-7-linux-x64.rpm


RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000 && \
    alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws 200000 && \
    alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000

ENV JAVA_HOME /usr/java/latest


