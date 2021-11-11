FROM ubuntu:14.04
MAINTAINER Anastas Dancha "anapsix@random.io"

## UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

## JAVA INSTALLATION
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" > /etc/apt/sources.list.d/webupd8team-java-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-recommends oracle-java8-installer && apt-get clean all

## JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
