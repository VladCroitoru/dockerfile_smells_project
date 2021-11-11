FROM docker:latest

# Java Version
ENV JAVA_VERSION=8 JAVA_UPDATE=151 JAVA_BUILD=12 JAVA_PACKAGE=server-jre JAVA_HOME=/usr/lib/jvm/default-jvm

# SBT environment
ENV SBT_VERSION=0.13.16
ENV SBT_HOME=/usr/local/sbt-launcher-packaging-0.13.16
ENV SBT_OPTS -Xms1G -Xmx2G -Xss1M -XX:+CMSClassUnloadingEnabled

# Set environment
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PATH=${PATH}:${SBT_HOME}/bin

# Copy apks
COPY /lib /var/cache/apk

# Install Glibc and server-jre 8
WORKDIR /usr/lib/jvm

RUN apk update && apk upgrade && \
    apk add --update bash wget curl tree git bc openjdk8-jre-base libgcc && \
    apk add --allow-untrusted /var/cache/apk/glibc-2.21-r2.apk && \
    apk add --allow-untrusted /var/cache/apk/glibc-bin-2.21-r2.apk && \
    /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib 

# Install sbt
RUN mkdir -p $SBT_HOME
RUN curl -sL "https://cocl.us/sbt-0.13.16.tgz" | gunzip | tar -x -C $SBT_HOME --strip-components=1

RUN sbt exit

WORKDIR /app
