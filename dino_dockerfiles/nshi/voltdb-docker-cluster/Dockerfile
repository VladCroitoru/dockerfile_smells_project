FROM ubuntu:16.04
MAINTAINER Ning Shi <nshi@voltdb.com>

# Public VoltDB ports
EXPOSE 22 5555 8080 8081 9000 21211 21212

# Internal VoltDB ports
EXPOSE 3021 4560 9090

# Set up environment
RUN apt-get update
RUN apt-get -y --no-install-recommends --no-install-suggests install sudo software-properties-common
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN apt-get install -y --no-install-recommends --no-install-suggests oracle-java8-installer
RUN apt-get install -y --no-install-recommends --no-install-suggests procps python vim
RUN locale-gen en_US.UTF-8

# Set VoltDB environment variables
ENV VOLTDB_DIST=/opt/voltdb
ENV PATH=$PATH:$VOLTDB_DIST/bin

# Set locale-related environment variables
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

# Set timezone
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Create necessary directories
RUN mkdir -p $VOLTDB_DIST
WORKDIR $VOLTDB_DIST
