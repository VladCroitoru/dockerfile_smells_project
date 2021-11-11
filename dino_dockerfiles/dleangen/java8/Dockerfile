# Installs java8 on a centos7.
# Based on https://www.digitalocean.com/community/tutorials/how-to-manually-install-oracle-java-on-a-debian-or-ubuntu-vps

FROM dleangen/centos7-systemd:0.1.0
LABEL maintainer "david@leangen.net"

# Base environment
ENV \
 HOME=/root \
 LANG=en_US.UTF-8 \
 LC_ALL=en_US.UTF-8

# Fundamental tools we need to create the build
RUN \
  yum install -y -q wget; \
  yum install -y -q deltarpm; \
  yum upgrade -y -q; \
  yum update -y -q;  \
  yum clean all -q;

# Setup the Java download
ENV \
  JDK_NUM=1.8.0 \
  JDK_REV=121 \
  JDK_VERSION=8u121\
  JDK_BUILD=b13 \
  JDK_HASH=e9e7ea248e2c4826b92b3f075a80e441

# Yuck!!
RUN \
  mkdir -p /opt/jdk; \
  wget --quiet --no-cookies --no-check-certificate --header \
    "Cookie: gpw_e24=http://www.oracle.com/; oraclelicense=accept-securebackup-cookie" \
    "http://download.oracle.com/otn-pub/java/jdk/${JDK_VERSION}-${JDK_BUILD}/${JDK_HASH}/jdk-${JDK_VERSION}-linux-x64.tar.gz"; \
  tar xzf jdk-${JDK_VERSION}-linux-x64.tar.gz -C /opt/jdk; \
  update-alternatives --install /usr/bin/java  java  /opt/jdk/jdk${JDK_NUM}_${JDK_REV}/bin/java 100; \
  update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk${JDK_NUM}_${JDK_REV}/bin/javac 100; \
  cd /opt/jdk; \
  ln -s jdk${JDK_NUM}_${JDK_REV}/ java;

# Setup the Java environment
ENV JAVA_HOME="/opt/jdk/java"
