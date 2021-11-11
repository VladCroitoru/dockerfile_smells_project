# Orcale JDK base image
#
# VERSION 20160613_1

FROM phusion/baseimage:latest

MAINTAINER Rene Nederhand <rene@cogfor.com>

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get -y install software-properties-common 
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update

# automatically accept oracle license
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
# and install java 8 oracle jdk
RUN apt-get -y install oracle-java8-installer oracle-java8-set-default 
RUN update-alternatives --display java
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
