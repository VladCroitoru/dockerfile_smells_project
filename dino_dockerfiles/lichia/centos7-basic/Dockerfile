# Install centos 7

FROM centos
MAINTAINER Lichia Lu <lichialu@gmail.com>
ENV container docker
RUN yum -y reinstall glibc-common
RUN yum install -y wget tar zip
RUN yum -y update; yum clean all;

# Install Oracle JDK 8
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.rpm && rpm -ivh jdk-8u51-linux-x64.rpm && rm -rf jdk-8u51-linux-x64.rpm
# Set the JAVA_HOME variable
ENV JAVA_HOME /usr/java/jdk1.8.0_45
