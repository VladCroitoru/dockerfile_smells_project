# use nodejs in China mainland, according to the silly network environment

FROM epsilony/baseimage

MAINTAINER Man YUAN <epsilony@epsilony.net>

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
