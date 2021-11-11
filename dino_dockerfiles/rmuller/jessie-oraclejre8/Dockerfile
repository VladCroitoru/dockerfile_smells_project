# Dockerfile for 'rmuller/jessie-oraclejre8'
FROM debian:jessie-slim
MAINTAINER Ronald K. Muller <rmuller@xiam.nl>
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle
ARG JAVA_UPDATE=112 
ARG JAVA_BUILD=15
ARG JAVA_FILE=server-jre-8u${JAVA_UPDATE}-linux-x64.tar.gz
RUN export DEBIAN_FRONTEND=noninteractive &&\
    apt-get update -qq &&\
    apt-get install -qq wget &&\
    wget --quiet --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
    "http://download.oracle.com/otn-pub/java/jdk/8u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_FILE}" &&\
    mkdir -p ${JAVA_HOME} &&\
    tar -C ${JAVA_HOME} --strip 2 -xf ${JAVA_FILE} jdk1.8.0_${JAVA_UPDATE}/jre &&\
    rm -Rf ${JAVA_FILE} &&\
    find ${JAVA_HOME}/bin/ ! -name 'java' -type f -delete &&\
    find ${JAVA_HOME}/lib/ -regex '.*\(Turbo\|RedHat\|SuSE\).*' -delete &&\
    ln -fsn ${JAVA_HOME}/bin/java /bin/java &&\
    apt-get autoremove --purge -qq wget &&\
    rm -rf /var/lib/apt/lists/* /var/log/apt/*
CMD /bin/bash









