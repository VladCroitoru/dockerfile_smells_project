FROM ubuntu:15.04
MAINTAINER Cyrille Le Clerc <cleclerc@cloudbees.com>

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#################################################
# Inspired by
# https://github.com/SeleniumHQ/docker-selenium/blob/master/Base/Dockerfile
#################################################


#================================================
# Customize sources for apt-get
#================================================
RUN  echo "deb http://archive.ubuntu.com/ubuntu vivid main universe\n" > /etc/apt/sources.list \
  && echo "deb http://archive.ubuntu.com/ubuntu vivid-updates main universe\n" >> /etc/apt/sources.list

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install software-properties-common \
  && add-apt-repository -y ppa:git-core/ppa

#========================
# Miscellaneous packages
# iproute which is surprisingly not available in ubuntu:15.04 but is available in ubuntu:latest
# OpenJDK8
# rlwrap is for azure-cli
# groff is for aws-cli
# tree is convenient for troubleshooting builds
#========================
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    iproute \
    openssh-client ssh-askpass\
    ca-certificates \
    openjdk-8-jdk \
    tar zip unzip \
    wget curl \
    git \
    build-essential \
    less nano tree \
    python python-pip groff \
    rlwrap \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' ./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security

# workaround https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=775775
RUN [ -f "/etc/ssl/certs/java/cacerts" ] || /var/lib/dpkg/info/ca-certificates-java.postinst configure

#==========
# Maven
#==========
ENV MAVEN_VERSION 3.3.9

RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

#========================================
# Add normal user with passwordless sudo
#========================================
RUN useradd builder --shell /bin/bash --create-home \
  && usermod -a -G sudo builder \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'builder:secret' | chpasswd


#====================================
# Cloud Foundry CLI
# https://github.com/cloudfoundry/cli
#====================================
RUN wget -O - "http://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -C /usr/local/bin -zxf -

#====================================
# AWS CLI
#====================================
RUN pip install awscli

# compatibility with CloudBees AWS CLI Plugin which expects pip to be installed as user
RUN mkdir -p /home/builder/.local/bin/ \
  && ln -s /usr/bin/pip /home/builder/.local/bin/pip \
  && chown -R builder:builder /home/builder/.local

#====================================
# NODE JS
# See https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
#====================================
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash \
    && apt-get install -y nodejs

#====================================
# BOWER, GRUNT, GULP
#====================================

RUN npm install --global grunt-cli@0.1.2 bower@1.7.9 gulp@3.9.1

USER builder
