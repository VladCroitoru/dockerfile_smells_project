############################################################
# Dockerfile to run TEAMCITY
# Based on Ubuntu Image
# Maintainer: Eftakhairul Islam <eftakhairul@gmail.com>
############################################################

# Base Image Ubuntu Trusty 14.04 (LTS) 
FROM ubuntu:14.04

# http://eftakhairul.com
MAINTAINER Eftakhairul Islam  <eftakhairul@gmail.com>

#Install utility libraries
RUN apt-get update && apt-get install -y \
    wget \
    tar \
    software-properties-common

# Install Java.
# Ref: https://github.com/dockerfile/java/tree/master/oracle-java7
RUN \
  echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java7-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk7-installer

# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle


#Teamcity data path
VOLUME  ["/data/teamcity"]
ENV TEAMCITY_DATA_PATH /data/teamcity

# Download and install TeamCity to /opt
#http://download-cf.jetbrains.com/teamcity/TeamCity-9.0.4.tar.gz
ENV TEAMCITY_PACKAGE TeamCity-9.0.4.tar.gz
ENV TEAMCITY_DOWNLOAD http://download.jetbrains.com/teamcity
RUN wget $TEAMCITY_DOWNLOAD/$TEAMCITY_PACKAGE && \
    tar zxf $TEAMCITY_PACKAGE -C /opt && \
    rm -rf $TEAMCITY_PACKAGE

#Expose the PORT 8111
EXPOSE 8111
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]