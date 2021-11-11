# Dockerfile for Java and Python based RDKit implementation
# Based on Debian.
# Includes InCHI support.
# WARNING: this takes about an hour to build

FROM informaticsmatters/rdkit:latest
MAINTAINER Tim Dudgeon <tdudgeon@informaticsmatters.com>

USER root

RUN apt-get update && apt-get install -y \
 openjdk-8-jdk &&\
 apt-get upgrade -y &&\
 apt-get clean -y

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

WORKDIR $RDBASE/build

RUN cmake -D RDK_BUILD_SWIG_WRAPPERS=ON -DRDK_BUILD_INCHI_SUPPORT=ON .. &&\
 make &&\
 make install

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RDBASE/Code/JavaWrappers/gmwrapper
ENV CLASSPATH=$RDBASE/Code/JavaWrappers/gmwrapper/org.RDKit.jar

#USER rdkit
WORKDIR $RDBASE 
