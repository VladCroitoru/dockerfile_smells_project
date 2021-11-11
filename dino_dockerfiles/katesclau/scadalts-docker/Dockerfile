FROM ubuntu:16.04

MAINTAINER Diego Ferreira version: 0.1

RUN ls -la
COPY ScadaBR.war /tmp/ScadaBR.war
COPY ScadaLTS.war /tmp/ScadaLTS.war
COPY context.xml /var/lib/tomcat7/conf
COPY start.sh /tmp/start.sh
ADD http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/mysql-connector-java-5.1.46.zip /tmp

RUN apt-get update && apt-get install -y \
  dos2unix \
  unzip \
  openjdk-8-jre \
  mariadb-client-10.0 \
  mariadb-server-10.0 \
  tomcat7 \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
  && unzip mysql-connector-java-5.1.46.zip \
  && cp mysql-connector-java-5.1.46/mysql-connector-java-5.1.46-bin.jar /usr/share/tomcat7/lib \
  && rm -rf /tmp/mysql*

ENV TOMCAT_RUN_USER tomcat7
ENV TOMCAT_RUN_GROUP tomcat7
ENV TOMCAT_LOG_DIR /var/log/tomcat7
ENV CATALINA_HOME /var/lib/tomcat7
ENV SCADALTS_VERSION 0.0.9.4

# Ensures that our script is runnable
RUN dos2unix /tmp/start.sh

EXPOSE 8080

ENTRYPOINT /tmp/start.sh
