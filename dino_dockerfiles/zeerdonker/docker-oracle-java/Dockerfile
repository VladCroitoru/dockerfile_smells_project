FROM        ubuntu:14.04

MAINTAINER  ZeerDonker

ENV         DEBIAN_FRONTEND noninteractive

# INSTALL OS DEPENDENCIES
RUN         apt-get update; apt-get install -y software-properties-common unzip

RUN         apt-get install -y vim 

# INSTALL JAVA 7
RUN         echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
            echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
            add-apt-repository -y ppa:webupd8team/java && \
            apt-get update && \
            apt-get install -y oracle-java8-installer
