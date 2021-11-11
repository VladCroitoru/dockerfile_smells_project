FROM phusion/baseimage:latest
MAINTAINER ZanyXdev "zanyxdev@gmail.com"

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Set environment variables 
ENV DEBIAN_FRONTEND noninteractive 

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections

RUN apt-get update && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:webupd8team/java && \
    apt-get update && \ 
    apt-get install -y --no-install-recommends oracle-java8-installer && \
    apt-get install oracle-java8-set-default

RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/oracle-jdk8-installer/*

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle
#ENV STUDIO_JDK=/usr/lib/jvm/java-8-oracle
ENV JDK_HOME=/usr/lib/jvm/java-8-oracle
ENV PATH=$PATH:$JAVA_HOME/bin

# Define default command.
CMD ["/sbin/my_init", "/bin/bash"]





