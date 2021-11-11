# Dockerfile for 'rmuller/jessie-oraclejdk8'
FROM debian:jessie-slim
MAINTAINER Ronald K. Muller <rmuller@xiam.nl>
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle
ARG JAVA_UPDATE=112 
ARG JAVA_BUILD=15
ARG JAVA_FILE=jdk-8u${JAVA_UPDATE}-linux-x64.tar.gz
ENV MAVEN_HOME=/usr/share/maven
ARG MAVEN_VERSION=3.3.9
RUN export DEBIAN_FRONTEND=noninteractive &&\
    apt-get update -qq &&\
    apt-get install -qq wget &&\
    mkdir -p ${JAVA_HOME} &&\
    wget -qO- --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
    "http://download.oracle.com/otn-pub/java/jdk/8u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_FILE}" |\
    tar -C ${JAVA_HOME} --strip 1 -xzf - &&\
    ln -fsn ${JAVA_HOME}/bin/java /bin/java &&\
    find ${JAVA_HOME} -maxdepth 1 -type f -delete &&\
    find ${JAVA_HOME}/jre -maxdepth 1 -type f -delete &&\
    find ${JAVA_HOME}/jre/bin ! -name "java" -type f -delete &&\
    find ${JAVA_HOME}/jre/lib -name "*ws*" -delete &&\
    find ${JAVA_HOME}/jre/lib -name "*fx*" -delete &&\
    find ${JAVA_HOME}/jre/lib/ -regex '.*\(Turbo\|RedHat\|SuSE\).*' -delete &&\
    rm ${JAVA_HOME}/jre/lib/deploy.jar &&\
    rm -Rf ${JAVA_HOME}/db ${JAVA_HOME}/lib/missioncontrol ${JAVA_HOME}/lib/visualvm \
           ${JAVA_HOME}/man ${JAVA_HOME}/jre/plugin ${JAVA_HOME}/jre/lib/deploy &&\
    mkdir ${MAVEN_HOME} &&\
    wget -qO- http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz \
    | tar -C ${MAVEN_HOME} --strip 1 -xzf - &&\
    ln -fsn ${MAVEN_HOME}/bin/mvn /bin/mvn &&\
    apt-get autoremove --purge -qq wget &&\
    rm -rf /var/lib/apt/lists/* /var/log/apt/*
CMD /bin/bash









