FROM ubuntu:15.04

MAINTAINER futabooo <mail@futabooo.com>

# Installing required packages
# https://source.android.com/source/initializing.html
RUN \
  apt-get update -y && \
  apt-get install -y git-core gnupg flex bison gperf build-essential \
  zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
  lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
  libgl1-mesa-dev libxml2-utils xsltproc unzip

# Install Java8, Java7, Java6
RUN \
  apt-get install -y openjdk-8-jdk openjdk-7-jdk openjdk-6-jdk

# Install Android SDK
RUN \
  cd /tmp && \
  curl -L -O http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz && \
  tar xf android-sdk_r24.4.1-linux.tgz -C /opt && \
  rm android-sdk_r24.4.1-linux.tgz && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter tools && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter platform-tools && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-26.0.2 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-25.0.2 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-25.0.1 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-25.0.0 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-24.0.2 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-24.0.0 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-23.0.3 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter build-tools-23.0.2 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter android-26 &&\
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter android-25 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter android-24 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter android-23 && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter extra-android-m2repository && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter extra-google-m2repository && \
  echo y | /opt/android-sdk-linux/tools/android update sdk --no-ui --all --filter extra-google-google_play_services

# Install Gradle
RUN \
  cd /tmp && \
  curl -L -O http://services.gradle.org/distributions/gradle-3.3-all.zip && \
  unzip gradle-3.3-all.zip -d /opt && \
  rm gradle-3.3-all.zip

# Make licenses directory
RUN mkdir /opt/android-sdk-linux/licenses

# Setup Environment
ENV JAVA8_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV JAVA7_HOME /usr/lib/jvm/java-7-openjdk-amd64
ENV JAVA6_HOME /usr/lib/jvm/java-6-openjdk-amd64
ENV JAVA_HOME $JAVA8_HOME
ENV ANDROID_HOME /opt/android-sdk-linux
ENV GRADLE_HOME /opt/gradle-3.3
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platfomr-tools:$GRADLE_HOME/bin
