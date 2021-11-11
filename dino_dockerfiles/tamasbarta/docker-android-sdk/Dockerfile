FROM openjdk:8

MAINTAINER Tamás Barta <barta.tamas.d@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -yq libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386 --no-install-recommends && \
    apt-get clean

# Download and untar SDK
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
RUN curl -L "${ANDROID_SDK_URL}" > android-sdk.zip
RUN unzip android-sdk.zip -d /usr/local/android-sdk-linux && rm android-sdk.zip
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV ANDROID_SDK /usr/local/android-sdk-linux
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH

# Install Android SDK components

ENV ANDROID_COMPONENTS "platform-tools build-tools;30.0.3 platforms;android-30"

RUN for component in ${ANDROID_COMPONENTS}; do echo y | /usr/local/android-sdk-linux/tools/bin/sdkmanager "${component}"; done

# Support Gradle
ENV TERM dumb
