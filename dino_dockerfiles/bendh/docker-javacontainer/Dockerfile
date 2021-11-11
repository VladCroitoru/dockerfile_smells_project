FROM fedora:23
MAINTAINER Ben Ooms <benoomsdh@gmail.com>

ENV JAVA_VERSION 7u80
ENV BUILD_VERSION b15

# Install utilities
RUN dnf install -y wget
# Downloading Java
RUN wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" -O /tmp/$JAVA_VERSION-linux-x64.rpm
RUN dnf install -y /tmp/$JAVA_VERSION-linux-x64.rpm
