FROM ubuntu:14.04

MAINTAINER Alex Melkonyan "sasha.melkonyan@gmail.com"

# Dismiss warning during installation
ENV DEBIAN_FRONTEND noninteractive

# Install java8
RUN apt-get update && apt-get install -y software-properties-common && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN add-apt-repository -y ppa:webupd8team/java
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get update && apt-get install -y oracle-java8-installer && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install unzip
RUN apt-get update && apt-get install -y unzip
# Install Deps
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y --force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 python curl && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Android SDK
RUN cd /opt && wget --output-document=android-sdk.zip --quiet https://dl.google.com/android/repository/tools_r25.2.3-linux.zip && unzip android-sdk.zip 

# Setup environment
ENV ANDROID_HOME /opt/android-sdk-linux
RUN mkdir -p ${ANDROID_HOME}
RUN cd /opt && mv tools/ ${ANDROID_HOME}/tools/
RUN cd /opt && rm -f android-sdk-tools.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools


RUN echo y | android update sdk --no-ui --all --filter platform-tools | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter android-25 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter android-24 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter android-23 | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.2 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.3 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.0 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.2 | grep 'package installed'


RUN echo y | android update sdk --no-ui --all --filter extra-android-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-google_play_services | grep 'package installed'

RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-23 | grep 'package installed'

# RUN which adb
# RUN which android

# Create emulator
# RUN echo "no" | android create avd \
#                --force \
#                --device "Nexus 5" \
#                --name test \
#                --target android-23 \
#                --abi armeabi-v7a \
#                --skin WVGA800 \
#               --sdcard 512M

# android uses this to figure out os bitness 
RUN export SHELL=/bin/bash

# Cleaning
RUN apt-get clean

# GO to workspace
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
