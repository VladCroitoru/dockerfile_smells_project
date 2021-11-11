# based on https://registry.hub.docker.com/u/samtstern/android-sdk/dockerfile/ with openjdk-8
FROM openjdk:8

MAINTAINER Saul Hernandez

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -yq libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386 --no-install-recommends && \
    apt-get clean

# Set android env varibales
ENV ANDROID_HOME /usr/local/android-sdk
ENV ANDROID_SDK /usr/local/android-sdk
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$PATH

# Download and untar SDK
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/tools_r25.2.3-linux.zip
RUN mkdir -p /usr/local/android-sdk
WORKDIR /usr/local/android-sdk
RUN wget "${ANDROID_SDK_URL}" 
RUN unzip tools_r25.2.3-linux.zip

# Install Android SDK components
RUN (while sleep 1; do echo "y"; done) | sdkmanager "platform-tools" "build-tools;26.0.0" "platforms;android-26" "extras;android;m2repository" "extras;google;m2repository" "extras;google;google_play_services" "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2"

# Make sure it's up to date
RUN (while sleep 1; do echo "y"; done) | sdkmanager --update

# Accept all licenses
RUN (while sleep 1; do echo "y"; done) | sdkmanager --licenses
