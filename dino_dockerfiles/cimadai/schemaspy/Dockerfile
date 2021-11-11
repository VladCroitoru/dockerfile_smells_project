FROM alpine:3.4

##############################
# Install java (open jdk)
##############################
# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN \
    { \
        echo '#!/bin/sh'; \
        echo 'set -e'; \
        echo; \
        echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
    } > /usr/local/bin/docker-java-home \
    && chmod +x /usr/local/bin/docker-java-home

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
ENV JAVA_VERSION 8u111
ENV JAVA_ALPINE_VERSION 8.111.14-r0

RUN \
    set -x && apk add --no-cache openjdk8="$JAVA_ALPINE_VERSION"

##############################
# Install graphviz & bash
##############################
RUN apk add --no-cache --update graphviz bash

##############################
# Install ja-font
##############################
ENV LANG ja_JP.UTF-8
COPY fonts.conf /root/.config/fontconfig/
COPY ipag.ttc /root/.local/share/fonts/
RUN apk add --no-cache fontconfig && fc-cache -fv

##############################
# Copy jars
##############################
COPY postgresql-42.2.1.jar /root/postgresql-42.2.1.jar
COPY schemaspy-6.0.0-rc2.jar /root/schemaspy-6.0.0-rc2.jar

##############################
# Copy script
##############################
COPY run_schemaspy.sh /root/run_schemaspy.sh
RUN chmod +x /root/run_schemaspy.sh

WORKDIR /root/

CMD /root/run_schemaspy.sh
