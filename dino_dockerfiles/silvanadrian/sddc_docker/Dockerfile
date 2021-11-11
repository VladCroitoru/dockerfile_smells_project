FROM      ubuntu:14.04
MAINTAINER Silvan Adrian "hallo@silvanadrian.ch"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y curl && \
    apt-get install -y wget && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    apt-get -qq update > /dev/null && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get -qq -y install oracle-java8-installer > /dev/null && \
    sudo apt-get install -y libvirt-bin && \
    sudo apt-get install -y git && \
    sudo apt-get install -y openssh-client

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
EXPOSE 8080

WORKDIR /

ADD SDDC-0.0.3.jar SDDC-0.0.3.jar
ADD Config.xml Config.xml
ADD LibVirtComputeConfigExample.xml LibVirtComputeConfigExample.xml
ADD LibVirtNetworkConfigExample.xml LibVirtNetworkConfigExample.xml
ADD LibVirtStorageConfigExample.xml LibVirtStorageConfigExample.xml

CMD java -jar -Dspring.profiles.active=dev *.jar
