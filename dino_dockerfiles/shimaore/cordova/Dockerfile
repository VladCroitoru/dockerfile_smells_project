FROM debian:testing
MAINTAINER Stéphane Alnet <stephane@shimaore.net>

# Inspired by and based on:
# https://github.com/lfuelling/android-sdk-docker
# https://github.com/Kallikrein/dockerfiles/blob/master/cordova/Dockerfile
# https://github.com/oren/docker-cordova/blob/master/Dockerfile

# Install Java.
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    openjdk-8-jdk-headless \
    lib32stdc++6 lib32z1 \
    ca-certificates \
    curl \
    git \
    make \
    unzip \
  && \
  rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Install Android SDK.
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV ANDROID_ZIP tools_r25.2.3-linux.zip
RUN \
  curl -O https://dl.google.com/android/repository/$ANDROID_ZIP && \
  unzip -d $ANDROID_HOME $ANDROID_ZIP && \
  rm $ANDROID_ZIP
ENV PATH $PATH:$ANDROID_HOME/tools

RUN \
  (yes | /usr/local/android-sdk-linux/tools/bin/sdkmanager --update) && \
  (yes | /usr/local/android-sdk-linux/tools/bin/sdkmanager \
    'build-tools;25.0.2' \
    'platforms;android-24' \
  )

# /usr/local/android-sdk-linux/tools/bin/sdkmanager --list

# Install Node.js.
RUN \
  git clone https://github.com/tj/n.git n.git && \
  cd n.git && \
  make install && \
  cd .. && \
  rm -rf n.git && \
  n 7.4.0

# Install NPM packages
RUN \
  npm install -g \
    # Install Cordova.
    cordova \
    # Install coffee-script
    # Used by https://github.com/metova/coffee-script-cordova-plugin
    coffee-script

# Opt out of telemetry.
RUN \
  cordova telemetry off

# Self-check, install gradle etc.
RUN \
  mkdir /opt/src && \
  cordova create hello && \
  cd hello && \
  cordova platform add android --save && \
  cordova build && \
  cordova requirements android && \
  cd /opt/src && \
  rm -rf hello
