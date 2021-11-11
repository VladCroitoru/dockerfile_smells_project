#Based on CentOS
FROM centos:latest

MAINTAINER André Luis Gomes <andrelugomes@gmail.com>

#Upgrading system
RUN yum -y install wget

#Downloading and install Java
RUN \
	wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm" -O jdk-7-linux-x64.rpm && \
	rpm -Uvh jdk-7-linux-x64.rpm && \
	rm jdk-7-linux-x64.rpm

ENV JAVA_HOME /usr/java/default

#Define ActiveQM Envs
ENV ACTIVEMQ_VERSION 5.13.3
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION
ENV ACTIVEMQ_HOME /opt/activemq

# Downloading and install ActiveMQ
RUN \
  	wget http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-bin.tar.gz && \
  	mkdir -p /opt && \
  	tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ && \
  	rm $ACTIVEMQ-bin.tar.gz && \
  	ln -s /opt/$ACTIVEMQ $ACTIVEMQ_HOME


WORKDIR $ACTIVEMQ_HOME
EXPOSE 61616 8161

#Running ActiveMQ
CMD ["/bin/bash", "-c", "bin/activemq console"]

