
# source 
FROM ubuntu:14.04

# pre install settings

# all package update
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y software-properties-common curl

# install java
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer
RUN update-java-alternatives -s java-8-oracle
RUN apt-get install oracle-java8-set-default

