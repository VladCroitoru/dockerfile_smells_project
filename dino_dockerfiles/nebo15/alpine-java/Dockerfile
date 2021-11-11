FROM gliderlabs/alpine:3.4
MAINTAINER Nebo#15 <support@nebo15.com>

# Important!  Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like `apt-get update` won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT=2016-10-14 \
    LANG=en_US.UTF-8 \
    TERM=xterm \
    HOME=/

# Install glibc
ENV GLIBC_VERSION=2.23-r3
RUN apk --update --no-cache add wget ca-certificates && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk -P /tmp && \
    apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk && \
    apk --purge del ca-certificates wget && \
    rm -r /tmp/glibc-${GLIBC_VERSION}.apk \
          /var/cache/apk/*

# Install Java
ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=101 \
    JAVA_VERSION_BUILD=13 \
    JAVA_PACKAGE=jdk
RUN mkdir /opt && \
    apk --update --no-cache add curl ca-certificates && \
    curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \
        http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
        | tar -xzf - -C /opt && \
    ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \
    apk --purge del ca-certificates curl && \
    rm -rf /opt/jdk/*src.zip \
           /opt/jdk/lib/missioncontrol \
           /opt/jdk/lib/visualvm \
           /opt/jdk/lib/*javafx* \
           /opt/jdk/jre/lib/plugin.jar \
           /opt/jdk/jre/lib/ext/jfxrt.jar \
           /opt/jdk/jre/bin/javaws \
           /opt/jdk/jre/lib/javaws.jar \
           /opt/jdk/jre/lib/desktop \
           /opt/jdk/jre/plugin \
           /opt/jdk/jre/lib/deploy* \
           /opt/jdk/jre/lib/*javafx* \
           /opt/jdk/jre/lib/*jfx* \
           /opt/jdk/jre/lib/amd64/libdecora_sse.so \
           /opt/jdk/jre/lib/amd64/libprism_*.so \
           /opt/jdk/jre/lib/amd64/libfxplugins.so \
           /opt/jdk/jre/lib/amd64/libglass.so \
           /opt/jdk/jre/lib/amd64/libgstreamer-lite.so \
           /opt/jdk/jre/lib/amd64/libjavafx*.so \
           /opt/jdk/jre/lib/amd64/libjfx*.so \
           /var/cache/apk/*


RUN { \
    echo '#!/bin/sh'; \
    echo 'set -e'; \
    echo; \
    echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
  } > /usr/local/bin/docker-java-home \
  && chmod +x /usr/local/bin/docker-java-home

ENV JAVA_HOME=/opt/jdk/jre \
    PATH=$PATH:/opt/jdk/bin:/opt/jdk/jre/bin
