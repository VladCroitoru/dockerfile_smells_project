FROM        zeerdonker/docker-oracle-java:latest

MAINTAINER  zeerdonker

ENV         ACTIVATOR_VERSION 1.3.2
ENV         DEBIAN_FRONTEND noninteractive

# INSTALL TYPESAFE ACTIVATOR
RUN         cd /tmp && \
            wget http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \
            unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d /usr/local && \
            mv /usr/local/activator-$ACTIVATOR_VERSION /usr/local/activator && \
            rm typesafe-activator-$ACTIVATOR_VERSION.zip
