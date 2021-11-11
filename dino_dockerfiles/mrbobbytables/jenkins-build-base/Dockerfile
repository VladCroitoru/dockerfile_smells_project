################################################################################
# jenkins-build-base: 1.0.3
# Date: 11/23/2015
# Docker Version: 1.9.1.0~trusty
#
# Description:
# Base build container for jenkins. Comes packaged with just git and docker.
################################################################################

FROM ubuntu:14.04
MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables

ENV VERSION_DOCKER=1.9.1-0~trusty               \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle        \
    DERBY_HOME=/usr/lib/jvm/java-8-oracle/db    \
    J2SDKDIR=/usr/lib/jvm/java-8-oracle         \
    J2REDIR=/usr/lib/jvm/java-8-oracle/jre      \
    JAVACPROOT=/usr/share/java                  \
    LC_ALL=en_US.UTF-8                          \
    PATH=$PATH:/usr/lib/jvm/java-8-oracle/bin:/usr/lib/jvm/java-8-oracle/db/bin:/usr/lib/jvm/java-8-oracle/jre/bin

RUN apt-get update                           \
 && apt-get -y install apt-transport-https   \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 2C52609D  \
 && echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >> /etc/apt/sources.list.d/docker.list \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886                                     \
 && echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/oracle-java.list        \
 && echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/oracle-java.list    \
 && echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections                                      \
 && echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections                                        \
 && locale-gen en_US.UTF-8            \
 && dpkg-reconfigure locales          \
 && apt-get update                    \
 && apt-get -y install                \
    docker-engine=$VERSION_DOCKER     \
    git                               \
    oracle-java8-installer            \
 && apt-get -y autoremove             \
 && apt-get -y autoclean              \
 && rm -rf /var/cache/oracle-jdk8-installer  \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
