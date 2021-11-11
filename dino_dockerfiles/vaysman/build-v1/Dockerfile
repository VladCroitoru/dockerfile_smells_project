FROM ubuntu:15.04

ENV DEBIAN_FRONTEND noninteractive
RUN ["apt-get", "update"]
RUN ["apt-get", "-yq", "install", "openjdk-8-jdk"]
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre
RUN ["apt-get", "-yq", "install", "maven"]
