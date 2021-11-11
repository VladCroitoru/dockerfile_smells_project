FROM phusion/baseimage:0.9.19

MAINTAINER Fernando Gil fgilg55@gmail.com

# Setup prerequisites (JRE, wget)
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:openjdk-r/ppa &&\
    apt-get update &&\
    apt-get -yq install openjdk-8-jre-headless wget &&\
    apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Add Flume as runit service
ADD run.sh /etc/service/flume/run
RUN chown root /etc/service/flume/run && chmod +x /etc/service/flume/run

# Download Flume distribution and remove unneccesary stuff
ENV FLUME_VERSION 1.6.0
ENV FLUME_DOWNLOAD_URL http://www-eu.apache.org/dist/flume/$FLUME_VERSION/apache-flume-$FLUME_VERSION-bin.tar.gz

RUN mkdir -p /opt/flume && wget $FLUME_DOWNLOAD_URL &&\
    tar xvf apache-flume-$FLUME_VERSION-bin.tar.gz -C /opt/flume --strip-components=1 &&\
    rm apache-flume-$FLUME_VERSION-bin.tar.gz &&\
    rm -Rf /opt/flume/docs

# Flume specific options
# ======================

# Agent name
ENV FLUME_AGENT agent

# Config folder (relative to /opt/flume)
ENV FLUME_CONF conf

# Config file
ENV FLUME_CONF_FILE conf/flume-conf.properties.template

# Additional flume-ng startup flags
ENV FLUME_OPTS -Dflume.root.logger=INFO,console

