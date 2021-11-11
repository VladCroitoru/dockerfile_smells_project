FROM ubuntu:14.04

MAINTAINER sala "saladinkzn@gmail.com"

ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools
ENV sdkVersion=r24.4.1
ENV buildTools=23.0.3

RUN apt-get update -qq && apt-get install -y --no-install-recommends openjdk-7-jdk wget lib32stdc++6 lib32z1 && apt-get clean

RUN cd /opt && wget https://dl.google.com/android/android-sdk_$sdkVersion-linux.tgz && \
    tar xzf android-sdk_$sdkVersion-linux.tgz && rm -f android-sdk_$sdkVersion-linux.tgz

RUN echo y | android update sdk --all --filter platform-tools,build-tools-$buildTools,android-23,extra-google-m2repository,extra-android-m2repository --no-ui --force

RUN mkdir /workdir
WORKDIR /workdir
VOLUME /workdir
