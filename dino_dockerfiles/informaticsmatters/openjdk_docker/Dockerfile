# OpenJDK image that includes the Docker engine binaries. Designed for Java apps that need to use Docker 
# e.g. using the docker-java library https://github.com/docker-java/docker-java 

FROM centos:7
MAINTAINER Tim Dudgeon <tdudgeon@informaticsmatters.com>

RUN yum -y update && yum -y install docker-client.x86_64 java-1.8.0-openjdk.x86_64

ENV JAVA_HOME /usr/lib/jvm/jre-openjdk/
