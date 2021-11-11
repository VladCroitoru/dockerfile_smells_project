FROM ubuntu:17.04


RUN apt-get update -qq

# Dependencies to execute Android builds
#RUN dpkg --add-architecture i386
#RUN apt-get update -qq
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386
RUN apt-get install -y openjdk-8-jdk wget expect git curl unzip software-properties-common

# Flutter depends on /usr/lib/x86_64-linux-gnu/libstdc++.so.6 version GLIBCXX_3.4.18
# if we don't specify this, the libstdc++6 we get is the wrong version
# https://github.com/flutter/flutter/issues/6207
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y \
  && apt-get update -qq \
  && apt-get install -y libstdc++6 lib32stdc++6 fonts-droid-fallback

# Gradle
RUN add-apt-repository ppa:cwchien/gradle -y \
  && apt-get update -qq \
  && apt-get install -y gradle \
  && gradle -v

# Download Android SDK tools into $ANDROID_SDK_HOME
RUN useradd -u 1000 -M -s /bin/bash android
RUN chown 1000 /opt

USER android
ENV ANDROID_SDK_HOME /opt/android-sdk-linux
ENV ANDROID_HOME /opt/android-sdk-linux

RUN cd /opt && wget -q https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -O android-sdk.tgz
RUN cd /opt && tar -xvzf android-sdk.tgz
RUN cd /opt && rm -f android-sdk.tgz

ENV PATH ${PATH}:${ANDROID_SDK_HOME}/tools:${ANDROID_SDK_HOME}/platform-tools:/opt/tools


# Install Android SDKs and other build packages

# Other tools and resources of Android SDK
#  you should only install the packages you need!
# To get a full list of available options you can use:
#  android list sdk --no-ui --all --extended
# (!!!) Only install one package at a time, as "echo y" will only work for one license!
#       If you don't do it this way you might get "Unknown response" in the logs,
#         but the android SDK tool **won't** fail, it'll just **NOT** install the package.
RUN echo y | android update sdk --no-ui --all --filter platform-tools | grep 'package installed'
#RUN echo y | android update sdk --no-ui --all --filter extra-android-support | grep 'package installed'

# SDKs
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter android-25 | grep 'package installed'

# build tools
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.3 | grep 'package installed'

# Android System Images, for emulators
# Please keep these in descending order!
#RUN echo y | android update sdk --no-ui --all --filter sys-img-x86_64-android-25 | grep 'package installed'
#RUN echo y | android update sdk --no-ui --all --filter sys-img-x86-android-25 | grep 'package installed'
#RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-25 | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-google_apis-25 | grep 'package installed'

# Extras
RUN echo y | android update sdk --no-ui --all --filter extra-android-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-m2repository | grep 'package installed'

# Copy install tools
COPY tools /opt/tools

#Copy accepted android licenses
COPY licenses ${ANDROID_SDK_HOME}/licenses

# Update SDK
RUN /opt/tools/android-accept-licenses.sh android update sdk --no-ui --obsolete --force

USER root

# Flutter
RUN cd /opt \
  && git clone https://github.com/flutter/flutter.git -b alpha --depth 1 \
  && rm -rf /opt/flutter/.git

ENV PATH=$PATH:/opt/flutter/bin

RUN apt-get clean

VOLUME ["/opt/android-sdk-linux"]
