# Docker image with Ubuntu 14.04 and Oracle Java 1.7
# https://github.com/fernandoacorreia/ubuntu-14.04-oracle-java-1.7

FROM ubuntu:14.04
MAINTAINER Fernando de Alcântara Correia <fernandoacorreia@gmail.com>

RUN \
  echo "Adding webupd8team repository..."  && \
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list  && \
  echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

RUN \
  echo "Updating packages..."  && \
  apt-get update  && \
  DEBIAN_FRONTEND=noninteractive apt-get upgrade -f -y --force-yes

RUN \
  echo "Installing Java..."  && \
  echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
  echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-java7-installer oracle-java7-set-default

RUN \
  echo "Cleaning up..."  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV JAVA_HOME /usr/lib/jvm/java-7-oracle

CMD ["java"]
