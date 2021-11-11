FROM centos:latest
MAINTAINER duffqiu@gmail.com

RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7
RUN yum -y  update
RUN yum install -y wget

RUN wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm"
RUN rpm -i jdk-7u79-linux-x64.rpm

ENV JAVA_HOME=/usr/java/jdk1.7.0_79 JRE_HOME=/usr/java/jdk1.7.0_79/jre PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin CLASSPATH=$CLASSPATH:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib

RUN rm -rf jdk-7u79-linux-x64.rpm

CMD [ "/bin/bash" ]
