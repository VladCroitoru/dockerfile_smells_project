FROM ubuntu:16.04

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
# https://github.com/cloudbees/java-build-tools-dockerfile/blob/master/Dockerfile#L28
#################################################


#================================================
# Customize sources for apt-get
#================================================
RUN DISTRIB_CODENAME=$(cat /etc/*release* | grep DISTRIB_CODENAME | cut -f2 -d'=') \
    && echo "deb http://archive.ubuntu.com/ubuntu ${DISTRIB_CODENAME} main universe\n" > /etc/apt/sources.list \
    && echo "deb http://archive.ubuntu.com/ubuntu ${DISTRIB_CODENAME}-updates main universe\n" >> /etc/apt/sources.list \
    && echo "deb http://security.ubuntu.com/ubuntu ${DISTRIB_CODENAME}-security main universe\n" >> /etc/apt/sources.list

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

# workaround "You are using pip version 8.1.1, however version 9.0.1 is available."
RUN pip install --upgrade pip setuptools

#==========
# Maven
#==========
ENV MAVEN_VERSION 3.3.9

RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

#==========
# Selenium
#==========

ENV SELENIUM_MAJOR_VERSION 3.0
ENV SELENIUM_VERSION 3.0.1
RUN  mkdir -p /opt/selenium \
  && wget --no-verbose http://selenium-release.storage.googleapis.com/$SELENIUM_MAJOR_VERSION/selenium-server-standalone-$SELENIUM_VERSION.jar -O /opt/selenium/selenium-server-standalone.jar

RUN pip install -U selenium

# https://github.com/SeleniumHQ/docker-selenium/blob/master/StandaloneFirefox/Dockerfile

ENV SCREEN_WIDTH 1360
ENV SCREEN_HEIGHT 1020
ENV SCREEN_DEPTH 24
ENV DISPLAY :99.0

COPY entry_point.sh /opt/bin/entry_point.sh
COPY functions.sh /opt/bin/functions.sh
RUN chmod +x /opt/bin/entry_point.sh \
  && chmod +x /opt/bin/functions.sh

#========================================
# Add normal user with passwordless sudo
#========================================
RUN useradd jenkins --shell /bin/bash --create-home \
  && usermod -a -G sudo jenkins \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'jenkins:secret' | chpasswd

#=====
# XVFB
#=====
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    xvfb \
  && rm -rf /var/lib/apt/lists/*

#=========
# Firefox
#=========
ARG FIREFOX_VERSION=50.1.0

# don't install firefox with apt-get because there are some problems,
# install the binaries downloaded from mozilla
# see https://github.com/SeleniumHQ/docker-selenium/blob/3.0.1-fermium/NodeFirefox/Dockerfile#L13
# workaround "D-Bus library appears to be incorrectly set up; failed to read machine uuid"
# run "dbus-uuidgen > /var/lib/dbus/machine-id"

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install firefox dbus \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2 \
  && apt-get -y purge firefox \
  && rm -rf /opt/firefox \
  && tar -C /opt -xjf /tmp/firefox.tar.bz2 \
  && rm /tmp/firefox.tar.bz2 \
  && mv /opt/firefox /opt/firefox-$FIREFOX_VERSION \
  && ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox

RUN dbus-uuidgen > /var/lib/dbus/machine-id

#======================
# Firefox GECKO DRIVER
#======================

ARG GECKO_DRIVER_VERSION=v0.13.0
RUN wget -O - "https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz" \
      | tar -xz -C /usr/bin


#====================================
# NODE JS
# See https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
#====================================
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash \
	&& apt-get install -y nodejs


ARG JENKINS_REMOTING_VERSION=3.5 

# See https://github.com/jenkinsci/docker-slave/blob/2.62/Dockerfile#L32 

RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/$JENKINS_REMOTING_VERSION/remoting-$JENKINS_REMOTING_VERSION.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

COPY jenkins-slave /usr/local/bin/jenkins-slave

RUN chmod +x /usr/local/bin/jenkins-slave ; mkdir -p /home/jenkins/.m2/repository ; chown -R jenkins:jenkins /home/jenkins
#VOLUME ["/home/jenkins/.m2/repository/"]
#WORKDIR /home/jenkins
#USER jenkins 

ENTRYPOINT ["/opt/bin/entry_point.sh", "/usr/local/bin/jenkins-slave"]

EXPOSE 4444
