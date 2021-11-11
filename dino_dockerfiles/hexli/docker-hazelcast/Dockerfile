# Docker Container
#
# Environment
## OS: CentOS 7.2.1511
## JVM: Oracle JDK 1.8.102

FROM centos:7.2.1511
MAINTAINER Hexiong Li<hexli@me.com>

ENV HZ_VERSION 3.7.2
ENV HZ_HOME /opt/hazelcast/
RUN mkdir -p $HZ_HOME
WORKDIR $HZ_HOME

USER root

RUN env
# Install basic tools
RUN yum install -y wget ; yum clean all
# Install Oracle JDK
RUN wget --quiet --no-cookies --no-check-certificate \
  --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" \
   "http://download.oracle.com/otn-pub/java/jdk/8u102-b14/jre-8u102-linux-x64.rpm" 
RUN yum install -y jre-8u102-linux-x64.rpm ; yum clean all
RUN rm -f jre-8u102-linux-x64.rpm

# Set environment variables.
ENV JAVA_HOME=/usr/java/default


# Add Hazelcast
ADD https://repo1.maven.org/maven2/com/hazelcast/hazelcast-all/$HZ_VERSION/hazelcast-all-$HZ_VERSION.jar $HZ_HOME
#ADD hazelcast.xml /$HZ_HOME/hazelcast.xml
ADD server.sh /$HZ_HOME/server.sh
RUN chmod +x /$HZ_HOME/server.sh
# Start hazelcast standalone server.
CMD ./server.sh
EXPOSE 5701
