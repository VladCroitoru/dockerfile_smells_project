FROM ubuntu:13.10
MAINTAINER Jesse xu, sxu11@ncsu.edu

RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" > /etc/apt/sources.list
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y wget openjdk-7-jdk curl unzip

RUN apt-get -y install git
RUN apt-get -y install maven
RUN apt-get -y install libblas*
RUN ldconfig /usr/local/cuda/lib64

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64