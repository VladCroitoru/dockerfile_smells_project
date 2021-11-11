# Dockerfile tutorbase
# Basic install Dockerfile for Git, Java Maven build
# 
FROM ubuntu:14.04
MAINTAINER Uta Kapp "uta.kapp@emooti.org"
RUN apt-get -y update
RUN apt-get -y install openjdk-7-jdk
ENV REFRESHED_AT 2017-03-03
ENV MAVEN_OPTS="-Xms512m -Xmx2048m -XX:MaxPermSize=512m"
ENV GIT_DISCOVERY_ACROSS_FILESYSTEM 1
RUN apt-get -y install wget
RUN apt-get -y install curl vim git maven
RUN mvn -version
