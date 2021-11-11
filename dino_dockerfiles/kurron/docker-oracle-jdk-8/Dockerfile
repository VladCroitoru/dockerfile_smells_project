# Use this as a base to solve the PID 1 problem 
FROM phusion/baseimage:0.9.15

MAINTAINER Ron Kurr <kurr@kurron.org>

ENV DEBIAN_FRONTEND noninteractive

# Install JDK 8 
RUN apt-get --quiet update && \
    apt-get --quiet --yes install wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    wget --quiet \
         --output-document=/jdk-8.tar.gz \
         --no-check-certificate \
         --no-cookies \
         --header "Cookie: oraclelicense=accept-securebackup-cookie" \
         http://download.oracle.com/otn-pub/java/jdk/8u101-b13/jdk-8u101-linux-x64.tar.gz && \
    mkdir -p /usr/lib/jvm && \
    tar --gunzip --extract --verbose --file /jdk-8.tar.gz --directory /usr/lib/jvm && \
    rm -f /jdk-8.tar.gz && \
    chown -R root:root /usr/lib/jvm

# set the environment variables 
ENV JDK_HOME /usr/lib/jvm/jdk1.8.0_101
ENV JAVA_HOME /usr/lib/jvm/jdk1.8.0_101
ENV PATH $PATH:$JAVA_HOME/bin

# used to set common JVM tunings
ENV JVM_HEAP_MIN 128m
ENV JVM_HEAP_MAX 512m
ENV JVM_METASPACE 512m
ENV JVM_CMS_OCCUPANCY 70
ENV JVM_GC_LOG_PATH /var/logs
ENV JVM_GC_LOG_FILE_COUNT 10
ENV JVM_GC_LOG_FILE_SIZE 100M
ENV JVM_DNS_TTL 30
ENV JVM_JMX_HOST 127.0.0.1
ENV JVM_JMX_PORT 9898
ENV JVM_JMX_RMI_PORT 9999

# Force Docker to use UTF-8 encodings
ENV LANG C.UTF-8

# export meta-data about this container
LABEL org.kurron.java.vendor="Oracle"  org.kurron.java.version="1.8.0_101"

ADD launch-jvm.sh /opt/launch-jvm.sh
WORKDIR /opt

