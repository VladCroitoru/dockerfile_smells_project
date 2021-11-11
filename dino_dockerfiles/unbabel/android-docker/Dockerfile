FROM ubuntu:16.04

MAINTAINER Ivan Bruel "ivan@unbabel.com"

# Based on https://github.com/appunite/docker and https://github.com/bitrise-docker/android/

ENV ANDROID_HOME /opt/android-sdk-linux

# Base pre-installed tools
RUN apt-get update -qq
# Required
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install git mercurial curl wget rsync sudo expect
# Common, useful
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install zip unzip
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tree
# For PPAs
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common

# Install required tools
RUN apt-get update -qq

# Install java8
RUN dpkg --add-architecture i386
RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386

# Install Ruby from source
# from source: mainly because of GEM native extensions,
# this is the most reliable way to use Ruby no Ubuntu if GEM native extensions are required
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev
RUN wget -q http://cache.ruby-lang.org/pub/ruby/ruby-2.3.3.tar.gz
RUN tar -xvzf ruby-2.3.3.tar.gz
RUN cd ruby-2.3.3 && ./configure --prefix=/usr/local && make && make install
# cleanup
RUN rm -rf ruby-2.3.3
RUN rm ruby-2.3.3.tar.gz
# install bundler
RUN gem install bundler --no-document

# Download Android SDK tools into $ANDROID_HOME
RUN cd /opt && wget -q https://dl.google.com/android/repository/tools_r25.2.4-linux.zip -O android-sdk-tools.zip
RUN cd /opt && unzip -q android-sdk-tools.zip
RUN mkdir -p ${ANDROID_HOME}
RUN cd /opt && mv tools/ ${ANDROID_HOME}/tools/
RUN cd /opt && rm -f android-sdk-tools.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

# Install Android Dependencies
# Other tools and resources of Android SDK
# you should only install the packages you need!
# To get a full list of available options you can use:
# android list sdk --no-ui --all --extended
# (!!!) Only install one package at a time, as "echo y" will only work for one license!
#       If you don't do it this way you might get "Unknown response" in the logs,
#       but the android SDK tool **won't** fail, it'll just **NOT** install the package.
RUN echo y | android update sdk --no-ui --all --filter platform-tools | grep 'package installed'

# SDKs
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter android-25 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter android-24 | grep 'package installed'

# build tools
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.2 | grep 'package installed'

# Android System Images, for emulators
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter sys-img-x86_64-google_apis-25 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-24 | grep 'package installed'

# Extras
RUN echo y | android update sdk --no-ui --all --filter extra-android-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-google_play_services | grep 'package installed'

# Accept Android licences
RUN mkdir "$ANDROID_HOME/licenses" || true
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "$ANDROID_HOME/licenses/android-sdk-license"
RUN echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_HOME/licenses/android-sdk-preview-license"

# Remove NDK ENV VARS
RUN unset ANDROID_NDK_HOME

# Install Gradle from PPA
RUN apt-get update
RUN apt-get -y install gradle
RUN gradle -v

# Install Maven 3 from PPA
RUN apt-get purge maven maven2
RUN apt-get update
RUN apt-get -y install maven
RUN mvn --version

# Install Fastlane
RUN gem install fastlane --no-document
RUN fastlane --version

# Install additional packages
# Required for Android ARM Emulator
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libqt5widgets5
ENV QT_QPA_PLATFORM offscreen
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:${ANDROID_HOME}/tools/lib64

# Git identity
RUN git config --global user.email ci@unbabel.com
RUN git config --global user.name "Unbabel CI"

# Cleaning
RUN apt-get clean

# GO to workspace
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
