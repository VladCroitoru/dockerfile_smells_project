# Android Dockerfile

FROM ubuntu:16.04

MAINTAINER Rogerio Angeliski "angeliski@hotmail.com"

# Sets language to UTF8 : this works in pretty much all cases
ENV LANG en_US.UTF-8
RUN locale-gen $LANG

ENV DOCKER_ANDROID_LANG en_US
ENV DOCKER_ANDROID_DISPLAY_NAME mobileci-docker

# Never ask for confirmations
ENV DEBIAN_FRONTEND noninteractive

# auto validate license
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

# update repos
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886

# Update apt-get
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get dist-upgrade -y

RUN dpkg --add-architecture i386
RUN apt-get update

# Installing packages
RUN apt-get install -y \
  oracle-java8-installer \
  autoconf \
  build-essential \
  bzip2 \
  curl \
  gcc \
  git \
  groff \
  lib32stdc++6 \
  lib32z1 \
  lib32z1-dev \
  lib32ncurses5 \
  libz1:i386 \
  libncurses5:i386 \
  libbz2-1.0:i386 \
  libstdc++6:i386 \
  libc6-dev \
  libgmp-dev \
  libmpc-dev \
  libmpfr-dev \
  libxslt-dev \
  libxml2-dev \
  m4 \
  make \
  ncurses-dev \
  ocaml \
  openssh-client \
  pkg-config \
  python-software-properties \
  rsync \
  software-properties-common \
  unzip \
  wget \
  zip \
  zlib1g-dev \
  git \
  npm \
  nodejs \
  nodejs-legacy \
  s3cmd \
  --no-install-recommends

RUN apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN npm cache clear

# Install Deps
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y --force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 python curl libqt5widgets5 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# To know all possibilities, just run: android list sdk --all
# Install Android SDK
RUN cd /opt && wget https://dl.google.com/android/repository/tools_r25.2.3-linux.zip && \
  unzip tools_r25.2.3-linux.zip -d android-sdk-linux && \
  rm tools_r25.2.3-linux.zip && \
    (echo y | android-sdk-linux/tools/android update sdk -u -a -t 1,2,3,6,10,14,16,23,32,33,34,35,36,38,124,160,166,167,168,169,170,171,172)


ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools
  
# Support Gradle
ENV TERM dumb
ENV GRADLE_OPTS "-XX:+UseG1GC -XX:MaxGCPauseMillis=1000"

# Install npm packages
RUN npm install -g npm@latest cordova ionic gulp bower grunt phonegap && npm cache clean

# Create dummy app to build and preload gradle and maven dependencies
RUN cd / && echo 'n' | ionic start --v2 project && cd /project && ionic platform add android && ionic build android && rm -rf * .??* 

# Add build user account, values are set to default below
ENV RUN_USER mobileci
ENV RUN_UID 5089

RUN id $RUN_USER || adduser --uid "$RUN_UID" \
    --gecos 'Build User' \
    --shell '/bin/sh' \
    --disabled-login \
    --disabled-password "$RUN_USER"

# Fix permissions
RUN chown -R $RUN_USER:$RUN_USER $ANDROID_HOME $ANDROID_SDK_HOME
RUN chmod -R a+rx $ANDROID_HOME $ANDROID_SDK_HOME

# Creating project directories prepared for build when running
# `docker run`
ENV PROJECT /project
RUN chown -R $RUN_USER:$RUN_USER $PROJECT
WORKDIR $PROJECT

USER $RUN_USER
RUN echo "sdk.dir=$ANDROID_HOME" > local.properties

WORKDIR /project
