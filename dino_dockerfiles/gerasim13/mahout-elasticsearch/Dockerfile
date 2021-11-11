FROM gerasim13/elasticsearch
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>

ENV MAHOUT 0.11.0
ADD http://apache-mirror.rbc.ru/pub/apache/mahout/${MAHOUT}/apache-mahout-distribution-${MAHOUT}.tar.gz /tmp/${MAHOUT}.tar.gz

ENV MAVEN 3.3.1
ADD http://ftp.fau.de/apache/maven/maven-3/${MAVEN}/binaries/apache-maven-${MAVEN}-bin.tar.gz /tmp/${MAVEN}.tar.gz

RUN apk update && apk add tar && \
    mkdir /tmp/${MAHOUT} && \
    mkdir /tmp/${MAVEN} && \
    tar -xzvf /tmp/${MAHOUT}.tar.gz -C /tmp/${MAHOUT} && \
    tar -xzvf /tmp/${MAVEN}.tar.gz -C /tmp/${MAVEN} && \
    cp -r /tmp/${MAHOUT}/* /usr/lib/mahout && \
    mv /tmp/${MAVEN}/* /usr/lib/mvn && \
    rm -rf /tmp/* /var/cache/apk/*

ENV MAHOUT_LOCAL true
ENV MAHOUT_HOME /usr/lib/mahout
ENV MAHOUT_BIN $MAHOUT_HOME/bin
ENV MAVEN_HOME /usr/lib/mvn
ENV MAVEN_BIN $MAVEN_HOME/bin
ENV PATH $PATH:$MAVEN_HOME:$MAVEN_BIN:$MAHOUT_HOME:$MAHOUT_BIN
