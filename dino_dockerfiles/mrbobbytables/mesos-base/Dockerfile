################################################################################
# mesos-base:1.2.0
# Date: 1/21/2016
# Mesos Version: 0.26.0-0.2.145.ubuntu1404
#
# Description:
# Base build for mesos related containers.
################################################################################

FROM mrbobbytables/ubuntu-base:1.1.0
MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables


ENV VERSION_MESOS=0.26.0-0.2.145.ubuntu1404     \
    VERSION_ZOOKEEPER=3.4.5+dfsg-1              \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle        \
    DERBY_HOME=/usr/lib/jvm/java-8-oracle/db    \
    J2SDKDIR=/usr/lib/jvm/java-8-oracle         \
    J2REDIR=/usr/lib/jvm/java-8-oracle/jre      \
    JAVACPROOT=/usr/share/java                  \
    LC_ALL=en_US.UTF-8                          \
    PATH=$PATH:/usr/lib/jvm/java-8-oracle/bin:/usr/lib/jvm/java-8-oracle/db/bin:/usr/lib/jvm/java-8-oracle/jre/bin

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E56151BF                                     \
 && echo "deb http://repos.mesosphere.io/ubuntu/ trusty main" >> /etc/apt/sources.list.d/mesosphere.list  \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886                                     \
 && echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/oracle-java.list        \
 && echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/oracle-java.list    \
 && echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections                                      \
 && echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections                                        \
 && locale-gen en_US.UTF-8        \
 && dpkg-reconfigure locales      \
 && apt-get -y update             \
 && apt-get -y install            \
    curl                          \
    mesos=$VERSION_MESOS          \
    oracle-java8-installer        \
    wget                          \
    zookeeper=$VERSION_ZOOKEEPER  \
 && apt-get clean                 \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
 && rm -rf /var/cache/oracle-jdk8-installer        \
 && rm -rf /etc/mesos/zk
