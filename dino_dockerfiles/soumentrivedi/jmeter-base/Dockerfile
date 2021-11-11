#
# Dockerfile for a base jmeter image
# 
# Usage:
# It forms the basis for other images

#

FROM ubuntu:14.04 
MAINTAINER Souman Trivedi soumen.trivedi@gmail.com 

# Describe the environment
ENV JDK_VERSION 1.7.0
ENV JMETER_VERSION 3.0

# Install the JDK
RUN apt-get update -y && apt-get install curl openjdk-7-jdk -y && cd /var/lib && \
  curl http://mirror.ox.ac.uk/sites/rsync.apache.org/jmeter/binaries/apache-jmeter-$JMETER_VERSION.tgz -o /var/lib/jmeter-$JMETER_VERSION.tgz && \
  tar xf jmeter-$JMETER_VERSION.tgz && \
  rm -f jmeter-$JMETER_VERSION.tgz && \
  ln -s /var/lib/apache-jmeter-$JMETER_VERSION /var/lib/apache-jmeter && \
  curl https://repo1.maven.org/maven2/kg/apc/cmdrunner/2.0/cmdrunner-2.0.jar --output /var/lib/apache-jmeter/lib/cmdrunner-2.0.jar && \
  curl https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-manager/0.10/jmeter-plugins-manager-0.10.jar --output /var/lib/apache-jmeter/lib/ext/jmeter-plugins-manager.jar && \
  java -cp /var/lib/apache-jmeter/lib/ext/jmeter-plugins-manager.jar org.jmeterplugins.repository.PluginManagerCMDInstaller && \
  sh /var/lib/apache-jmeter/bin/PluginsManagerCMD.sh status && \
  sh /var/lib/apache-jmeter/bin/PluginsManagerCMD.sh install jpgc-casutg

ENTRYPOINT /bin/sh