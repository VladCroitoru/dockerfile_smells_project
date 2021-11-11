#    ______________________   ____                      __                __   _________            __ 
#   /  _/ ____/ ____/ ____/  / __ \____ _      ______  / /___  ____ _____/ /  / ____/ (_)__  ____  / /_
#   / // /   / / __/ /      / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  /  / /   / / / _ \/ __ \/ __/
# _/ // /___/ /_/ / /___   / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  / /___/ / /  __/ / / / /_  
#/___/\____/\____/\____/  /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/   \____/_/_/\___/_/ /_/\__/ 
                                   
# Banner @ http://goo.gl/VCY0tD

FROM       ubuntu:14.04
MAINTAINER ICGC <dcc-support@icgc.org>

ENV EGA_VERSION 2.2.2
ENV GT_VERSION 3.8.7
ENV GT_VERSION_LONG 207
#
# Update apt, add FUSE support, requiered libraries and basic command line tools
#

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y libfuse-dev fuse curl wget software-properties-common && \
  apt-get install libicu52 && \
# Required for Genetorrent and Icgc
  apt-get install unzip
# Required to download EGA

#
# Install OpenSSL for Genetorrent
#

RUN apt-get install openssl

#
# Install Oracle JDK 8 for icgc-storage client 
#

RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update && apt-get upgrade -y
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y \
    oracle-java8-installer \
    oracle-java8-set-default
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

#
# Install python 2.7 and dependancies for Genetorrent.
#

RUN apt-get install -y python && \
    wget -qO- http://pyyaml.org/download/pyyaml/PyYAML-3.11.tar.gz | \
    tar xvz --strip-components 1 && \
    python setup.py install && \
    mkdir -p /icgc/cli/clients

COPY /lib/cli/ /icgc/cli/

ENV PATH=$PATH:/icgc/cli

#
# Download and install latest EGA download client version
#

RUN mkdir -p /icgc/ega-download-demo && \
    cd /icgc/ega-download-demo && \
    wget -qO- https://www.ebi.ac.uk/ega/sites/ebi.ac.uk.ega/files/documents/EgaDemoClient_$EGA_VERSION.zip -O temp.zip ; \
    unzip temp.zip -d /icgc/ega-download-demo; \
    rm temp.zip

#
# Install GeneTorrent and add to PATH
#

RUN mkdir -p /icgc/genetorrent && \
    cd /icgc/genetorrent && \
    wget -qO- https://cghub.ucsc.edu/software/downloads/GeneTorrent/$GT_VERSION/GeneTorrent-download-$GT_VERSION-$GT_VERSION_LONG-Ubuntu14.04.x86_64.tar.gz | \
    tar xvz --strip-components 1 
ENV PATH=$PATH:/icgc/genetorrent/bin

# 
# Install latest version of storage client distribution
#

RUN mkdir -p /icgc/icgc-storage-client && \
    cd /icgc/icgc-storage-client && \
    wget -qO- https://seqwaremaven.oicr.on.ca/artifactory/dcc-release/org/icgc/dcc/icgc-storage-client/[RELEASE]/icgc-storage-client-[RELEASE]-dist.tar.gz | \
    tar xvz --strip-components 1

RUN mkdir -p /icgc/gdc-data-transfer-tool && \
    cd /icgc/gdc-data-transfer-tool && \ 
    wget -qO- https://gdc.nci.nih.gov/files/public/file/gdc-clientv07ubuntu1404x64_1.zip -O temp.zip ; \
    unzip temp.zip -d /icgc/gdc-data-transfer-tool ; \
    rm temp.zip
ENV PATH=$PATH:/icgc/gdc-data-transfer-tool

#
# Install latest version of gdc download tool
#

RUN mkdir -p /icgc/gdc-data-transfer-tool && \
    cd /icgc/gdc-data-transfer-tool && \
    wget -qO- https://gdc.nci.nih.gov/files/public/file/gdc-clientv07ubuntu1404x64_1.zip -O temp.zip ; \
    unzip temp.zip -d /icgc/gdc-data-transfer-tool ; \
    rm temp.zip

#
# Set working directory for convenience with interactive usage
#

WORKDIR /icgc


