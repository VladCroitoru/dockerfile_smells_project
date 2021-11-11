# Based on: https://registry.hub.docker.com/u/adamalex/play-docker-ci/

FROM        ubuntu:14.04

MAINTAINER  Andrea Sosso <andrea.sosso@dnshosting.it>

ENV         ACTIVATOR_VERSION 1.2.12
ENV         JAVA_VERSION 8
ENV         DEBIAN_FRONTEND noninteractive

# INSTALL OS DEPENDENCIES, JAVA AND TYPESAFE ACTIVATOR
RUN			apt-get update && \
	        apt-get install -y software-properties-common unzip && \
			add-apt-repository -y ppa:webupd8team/java && \
	        echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
            echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
			apt-get update && \
			apt-get install -y oracle-java$JAVA_VERSION-installer && \
            cd /tmp && \
            wget http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \
            unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d /usr/local && \
            mv /usr/local/activator-$ACTIVATOR_VERSION /usr/local/activator && \
            rm typesafe-activator-$ACTIVATOR_VERSION.zip && \
            apt-get clean && \
    		rm -rf /var/lib/apt/lists/*