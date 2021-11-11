# AlpineLinux with a glibc-2.21 and Oracle Java 8

FROM alpine:3.2
MAINTAINER Anastas Dancha [...]

COPY ./glibc-2.21-r2.apk /tmp/glibc-2.21-r2.apk
COPY jre-8u45-linux-x64.tar.gz /tmp/jre-8u45-linux-x64.tar.gz

# Install cURL
#RUN apk --update add curl ca-certificates tar && \
#    curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \
RUN apk --update add tar && \
    apk add --allow-untrusted /tmp/glibc-2.21-r2.apk

# Java Version
ENV JAVA_VERSION_MAJOR 8
ENV JAVA_VERSION_MINOR 45
ENV JAVA_VERSION_BUILD 14

# Install Java
RUN mkdir /opt
RUN tar -xzf /tmp/jre-8u45-linux-x64.tar.gz -C /opt &&\
    ln -s /opt/jre1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk &&\
    rm -rf /opt/jdk/*src.zip \
           /opt/jdk/lib/missioncontrol \
           /opt/jdk/lib/visualvm \
           /opt/jdk/lib/*javafx* \
           /opt/jdk/lib/plugin.jar \
           /opt/jdk/lib/ext/jfxrt.jar \
           /opt/jdk/bin/javaws \
           /opt/jdk/lib/javaws.jar \
           /opt/jdk/lib/desktop \
           /opt/jdk/plugin \
           /opt/jdk/lib/deploy* \
           /opt/jdk/lib/*javafx* \
           /opt/jdk/lib/*jfx* \
           /opt/jdk/lib/ext/nashorn.jar \
           /opt/jdk/lib/amd64/libdecora_sse.so \
           /opt/jdk/lib/amd64/libprism_*.so \
           /opt/jdk/lib/amd64/libfxplugins.so \
           /opt/jdk/lib/amd64/libglass.so \
           /opt/jdk/lib/amd64/libgstreamer-lite.so \
           /opt/jdk/lib/amd64/libjavafx*.so \
           /opt/jdk/lib/amd64/libjfx*.so \
	   /tmp/jre-8u45-linux-x64.tar.gz \
	   /tmp/glibc-2.21-r2.apk

# Hack to report vulnerabilities
# include ssl libraries that have vulnerabilities
COPY ./vulnerable-ssl-libs/*.* /usr/tempv/

# Set environment
ENV JAVA_HOME /opt/jdk
ENV PATH ${PATH}:${JAVA_HOME}/bin

WORKDIR /home

LABEL x="a"

ADD jdbc_code/build/JDBCExample.class JDBCExample.class
ADD mysql-connector-java-5.1.38-bin.jar mysql-connector-java-5.1.38-bin.jar
EXPOSE 8080
CMD "java" "-cp" ".:mysql-connector-java-5.1.38-bin.jar" "JDBCExample"
