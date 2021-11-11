FROM ubuntu:14.04.1
MAINTAINER momo <googolmo@gmail.com>

# install dependencies

RUN dpkg --add-architecture i386 && apt-get update \
      && apt-get install -y wget zip openjdk-7-jdk \
      libncurses5:i386 libstdc++6:i386 zlib1g:i386 \
      && apt-get clean autoclean && apt-get autoremove -y 
      && rm -rf /var/lib/{apt,dpkg,cache,log}

# install Android SDK
ENV ANDROID_SDK_VERSION 24.1.2

RUN cd /usr/local \
      && wget https://dl.google.com/android/android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz \
      && tar -xvf android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz \
      && rm -rvf android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz

ENV ANDROID_HOME /usr/local/android-sdk-linux

RUN echo y | ${ANDROID_HOME}/tools/android update sdk -a -u -t tools
RUN echo y | ${ANDROID_HOME}/tools/android update sdk -a -u -t platform-tools
RUN rm -rvf ${ANDROID_HOME}/temp/*

ENV PATH $PATH:$ANDROID_HOME/tools:
ENV PATH $PATH:$ANDROID_HOME/platform-tools
