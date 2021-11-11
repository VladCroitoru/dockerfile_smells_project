FROM centos:7
MAINTAINER Drew Fradette <drew.fradette@gmail.com>

VOLUME ["/data"]

RUN yum -y install wget
RUN wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u31-b13/jdk-8u31-linux-x64.rpm" -O /tmp/jdk-8-linux-x64.rpm
RUN yum -y install /tmp/jdk-8-linux-x64.rpm
RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws 200000
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000
ENV JAVA_HOME /usr/java/latest

RUN wget -O /tmp/spark.tgz http://www.eu.apache.org/dist/spark/spark-1.4.1/spark-1.4.1-bin-hadoop2.6.tgz
RUN tar xvzf /tmp/spark.tgz
RUN mv /spark-1.4.1-bin-hadoop2.6 /spark

WORKDIR /spark
RUN cp conf/log4j.properties.template conf/log4j.properties
RUN sed -i 's/INFO/WARN/' conf/log4j.properties
