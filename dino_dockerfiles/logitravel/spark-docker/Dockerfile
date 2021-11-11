FROM alpine:3.5

LABEL MAINTAINER Cristòfol Torrens Morell "piffall@gmail.com"
LABEL CONTRIBUTOR Vicenç Juan Tomàs Monserrat "vtomasr5@gmail.com"

LABEL STB_VERSION=0.13.13
LABEL SPARK_VERSION=2.2.0
LABEL HADOOP_VERSION=2.7

# Install required packages
RUN \
    apk update && \
    apk add openjdk8 wget bash tar gzip dcron

WORKDIR /opt

# Install SBT
ENV SBT_VERSION 0.13.15
ENV SBT_HOME /opt/sbt
RUN \
    mkdir -p /opt && \
    wget https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz && \
    tar -zvxf sbt-${SBT_VERSION}.tgz -C /opt && \
    rm sbt-${SBT_VERSION}.tgz

# Add sbt bin path to PATH
ENV PATH $PATH:${SBT_HOME}/bin

# Install Spark
ENV SPARK_VERSION 2.2.0
ENV HADOOP_VERSION 2.7
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}
RUN \
    mkdir ${SPARK_HOME} && \
    wget http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar vxzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz --strip 1 -C ${SPARK_HOME} && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Copy scripts
COPY start-master /usr/bin/start-master
COPY start-worker /usr/bin/start-worker
COPY start-driver /usr/bin/start-driver

# Add spark bin path to PATH
ENV PATH $PATH:${SPARK_HOME}/bin

# Set Java HOME
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk

