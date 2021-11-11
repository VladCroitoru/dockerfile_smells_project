FROM centos:centos7 
MAINTAINER Maikel Alderhout  <malderhout@gmail.com>

# UPDATE
RUN yum -y update  

# INSTALL packages 
RUN yum -y install wget
RUN yum -y install tar

# INSTALL JAVA
RUN yum -y install java-1.7.0-openjdk  

# TOMCAT version
ENV TOMCAT_VERSION 7.0.55

# INSTALL TOMCAT
RUN wget -q https://archive.apache.org/dist/tomcat/tomcat-7/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/catalina.tar.gz

# UNPACK
RUN tar xzf /tmp/catalina.tar.gz -C /opt
RUN ln -s /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat
RUN rm /tmp/catalina.tar.gz

# REMOVE APPS 
RUN rm -rf /opt/tomcat/webapps/examples /opt/tomcat/webapps/docs 

# SET CATALINE_HOME and PATH 
ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin

# SET PORT and start TOMCAT
EXPOSE 8080
EXPOSE 22
CMD $CATALINA_HOME/bin/catalina.sh run
