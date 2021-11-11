FROM alpine:3.8
MAINTAINER Jeff Harwell <jeff.harwell@gmail.com>

RUN apk --update add openjdk8-jre bash python3 netcat-openbsd

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk


RUN wget https://archive.apache.org/dist/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz && \
    tar -xvf ./spark-2.3.2-bin-hadoop2.7.tgz && \
    mkdir /opt && \
    mv ./spark-2.3.2-bin-hadoop2.7 /opt/ && \
    ln -s /opt/spark-2.3.2-bin-hadoop2.7 /opt/spark && \
    rm ./spark-2.3.2-bin-hadoop2.7.tgz

COPY start-worker /
COPY start-master /
COPY write_configuration.py /

RUN chmod +x /start-worker && \
    chmod +x /start-master && \
    chmod +x /write_configuration.py
