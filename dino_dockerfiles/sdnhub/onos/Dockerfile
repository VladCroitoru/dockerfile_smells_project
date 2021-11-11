# Base the image on Debian as it's pretty small
# Version 0.2.0
FROM debian
MAINTAINER Srini <srini@sdnhub.org>

# Install required software
ENV DEBIAN_FRONTEND noninteractive
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    apt-get update && \
    apt-get install -y oracle-java8-installer oracle-java8-set-default && \
    apt-get clean && apt-get purge

# Change to /root directory
WORKDIR /root

# Install ONOS
RUN mkdir onos && \
   wget http://sdnhub.org/downloads/tutorials/onos/onos-1.1.0-rc2.ubuntu.tar.gz && \
   tar -xf onos-1.1.0-rc2.ubuntu.tar.gz -C onos --strip-components=1 && \
   rm -rf onos-1.1.0-rc2.ubuntu.tar.gz

# Set the environment variables
ENV HOME /root
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV ONOS_NIC 172.17.*.*
ENV ONOS_ROOT /root/onos
ENV KARAF_VERSION 3.0.2
ENV KARAF_ROOT /root/onos/apache-karaf-3.0.3
ENV KARAF_LOG /root/onos/apache-karaf-3.0.3/data/log/karaf.log
ENV PATH $PATH:$KARAF_ROOT/bin

# Update the hazelcast xml
RUN sed -i "s/172.17.\*.\*/$ONOS_NIC/g" ${ONOS_ROOT}/apache-karaf-3.0.3/etc/hazelcast.xml

# Ports
# 6633 - OpenFlow
# 5701 - Hazelcast
EXPOSE 6633 5701

# Get ready to run command
WORKDIR /root/onos
CMD ["./bin/onos-service"]
