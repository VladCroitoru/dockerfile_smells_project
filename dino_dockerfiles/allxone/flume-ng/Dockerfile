FROM centos:6.6
MAINTAINER allxone@hotmail.com

# Install packages
RUN yum -y install wget tar && yum clean all

# Install JDK
RUN wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u75-b13/jdk-7u75-linux-x64.rpm" && rpm -Uvh jdk-7u75-linux-x64.rpm && rm -f jdk-7u75-linux-x64.rpm && /usr/sbin/alternatives --install "/usr/bin/java" "java" "/usr/java/jdk1.7.0_75/bin/java" 3 && /usr/sbin/alternatives --install "/usr/bin/javac" "javac" "/usr/java/jdk1.7.0_75/bin/javac" 3

# Install Flume
RUN curl http://apache.panu.it/flume/1.5.2/apache-flume-1.5.2-bin.tar.gz | tar xz -C /usr/local

# Start Flume
ENV FLUME_AGENT agent
ENV FLUME_CONF_FILE conf/flume-conf.properties.template
ENV JAVA_HOME /usr/java/jdk1.7.0_75

WORKDIR /usr/local/apache-flume-1.5.2-bin
ENTRYPOINT bin/flume-ng agent -n $FLUME_AGENT -c conf -f $FLUME_CONF_FILE

