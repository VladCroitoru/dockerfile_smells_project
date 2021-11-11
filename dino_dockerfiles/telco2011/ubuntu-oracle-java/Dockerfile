FROM ubuntu:latest
MAINTAINER David Lopez <davidlopez.david@gmail.com>

# Configure ubuntu
RUN apt-get install -y software-properties-common

# Enable silent install
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections

# setup Oracle Java
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update

# Java 8
RUN apt-get install -y oracle-java8-installer
# Not always necessary, but just in case...
RUN update-java-alternatives -s java-8-oracle
# Setting Java environment variables
RUN apt-get install -y oracle-java8-set-default

RUN java -version