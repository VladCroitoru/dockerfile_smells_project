FROM jenkins/jenkins:lts

MAINTAINER Andi Santoso (asantoso@thetestguys.com)

# change to root to install tools
USER root

# install wget
RUN apt-get update && apt-get install -y wget

# get maven 3.5.0
ENV maven_version 3.5.0
ENV maven_checksum 35c39251d2af99b6624d40d801f6ff02
RUN wget --no-verbose -O /tmp/apache-maven-${maven_version}.tar.gz http://archive.apache.org/dist/maven/maven-3/${maven_version}/binaries/apache-maven-${maven_version}-bin.tar.gz

# verify checksum
RUN echo "${maven_checksum} /tmp/apache-maven-${maven_version}.tar.gz" | md5sum -c

# install maven
RUN tar xzf /tmp/apache-maven-${maven_version}.tar.gz -C /opt/
RUN ln -s /opt/apache-maven-${maven_version} /opt/maven
RUN ln -s /opt/maven/bin/mvn /usr/local/bin
RUN rm -f /tmp/apache-maven-${maven_version}.tar.gz
ENV MAVEN_HOME /opt/maven

# install git
RUN apt-get install -y git

# install nano
RUN apt-get install -y nano

# remove download archive files
RUN apt-get clean

# switch back to jenkins user
USER jenkins

# disable security for Jenkins 2.x
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false

# configure Jenkins plugins
RUN /usr/local/bin/install-plugins.sh maven-plugin git htmlpublisher
