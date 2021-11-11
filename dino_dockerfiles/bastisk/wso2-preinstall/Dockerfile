# Dockerfile for installation of WSO2 Preinstallation Needs running on Ubuntu 14.04
# ================================================================
# File created by: Sebastian Kiepsch
# Last Edited: 25.03.2015, w8
# Procedure:
#	1. Install Oracle Java
#	2. Install Ant
#	3. Install Maven
#	4. Install ActiveMQ


FROM ubuntu:14.04
MAINTAINER Sebastian Kiepsch <basti.sk@gmx.de>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt-get -y upgrade
 
# ========== 1. Install Oracle Java ==========
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN apt-get install oracle-java7-installer -y
RUN apt-get install oracle-java7-set-default -y
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle

# ========== 2. Install Ant ==========
RUN apt-get -y install ant -y

# ========== 3. Install Maven ==========
RUN apt-get install maven -y
#ENV M2_HOME /opt/apache-maven-3.0.3
#ENV PATH ${M2_HOME}/bin:${PATH}



# ========== 4. Install ActiveMQ ==========
RUN apt-get install activemq -y
RUN service activemq restart

#RUN wget http://www.apache.org/dist/activemq/apache-activemq/5.5.1/apache-activemq-5.5.1-bin.tar.gz
#RUN tar -zxvf apache-activemq-5.5.1-bin.tar.gz
#WORKDIR /opt/
#RUN chmod 755 activemq
#RUN sh activemq start



