# VERSION 0.2
# AUTHOR:       Thomas Harning Jr <harningt@gmail.com>
# DESCRIPTION:  Build image with necessities to build the Atomun components

FROM alpine:3.9
MAINTAINER Thomas Harning Jr <harningt@gmail.com>

# NOTE: Versions not hardcoded as it is unimportant for the atomun builds at the moment

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

ENV JAVA7_HOME /usr/lib/jvm/java-1.7-openjdk

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV JAVA8_HOME /usr/lib/jvm/java-1.8-openjdk

# Install necessary pieces for build from Alpine
# - Git of course
# - Gnupg may be required for protected data management / verification
# - Java 7 - for backwards compatibility data
# - Java 8 - for modernity
# - Gradle expects bash, not simply sh
# - pip is used for codecov


RUN apk add --no-cache \
        git \
        gnupg \
        openjdk7 \
        openjdk8 \
        bash \
        py-pip

# Use PIP to install codecov
RUN pip install codecov
