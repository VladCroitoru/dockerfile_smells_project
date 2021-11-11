# You know you love it
FROM ubuntu:14.04

# Me, Myself and I
MAINTAINER Paulo Pires <pjpires@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get upgrade -y

# Install Oracle JRE 8
RUN apt-get -y install software-properties-common && \
    add-apt-repository ppa:webupd8team/java && \
    apt-get -y update && \
    echo "oracle-java8-installer  shared/accepted-oracle-license-v1-1 boolean true" | debconf-set-selections && \
    apt-get -y install oracle-java8-installer wget && \
    apt-get install oracle-java8-set-default && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/oracle-jdk8-installer

# enabling sudo group
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
# enabling sudo over ssh
RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers

# Add apollo user with sudo permissions
RUN adduser --disabled-password --gecos '' apollo
RUN adduser apollo sudo

# command line goodies
RUN echo "export JAVA_HOME=/usr/lib/jvm/jre" >> /etc/profile
RUN echo "alias ll='ls -l --color=auto'" >> /etc/profile
RUN echo "alias grep='grep --color=auto'" >> /etc/profile

# Download, extract and install Apollo MQ
WORKDIR /home/apollo
USER apollo
RUN wget -c http://www.eu.apache.org/dist/activemq/activemq-apollo/1.7/apache-apollo-1.7-unix-distro.tar.gz && \
    tar -zxvf apache-apollo-1.7-unix-distro.tar.gz && \
    rm apache-apollo-1.7-unix-distro.tar.gz
RUN apache-apollo-1.7/bin/apollo create mybroker
WORKDIR /home/apollo/mybroker
# TODO remove unsecured endpoints
EXPOSE 61613 61614 61623 61624 61680 61681

CMD  bin/apollo-broker run
