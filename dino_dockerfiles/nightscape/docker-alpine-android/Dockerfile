FROM frolvlad/alpine-oraclejdk8

ENV ANDROID_HOME /opt/android-sdk-linux

ENV PATH $PATH:$ANDROID_HOME/tools
ENV PATH $PATH:$ANDROID_HOME/platform-tools

# https://github.com/yongjhih/docker-android/blob/master/ubuntu-openjdk-8-android/Dockerfile
ENV ANDROID_SDK_ZIP http://dl.google.com/android/android-sdk_r24.3.4-linux.tgz

RUN apk add --no-cache curl ca-certificates bash libstdc++ && \
    mkdir -p /opt && curl -L $ANDROID_SDK_ZIP | tar zxv -C /opt
    # apk add --nocache lib32stdc++6 lib32z1

# https://github.com/yongjhih/docker-android/blob/master/ubuntu-openjdk-8-android-extra/Dockerfile
RUN echo "y" | android update sdk -u -a -t tools,platform-tools,extra-android-support,extra-android-m2repository,extra-google-google_play_services,extra-google-m2repository,extra-google-analytics_sdk_v2

ARG ANDROID_BUILD_TOOLS_VERSION=24.0.1
ARG ANDROID_APIS="android-10,android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24"

RUN echo "y" | android update sdk -u -a -t build-tools-${ANDROID_BUILD_TOOLS_VERSION},${ANDROID_APIS}