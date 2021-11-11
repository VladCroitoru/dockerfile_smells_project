FROM ubuntu:17.04

# ------------------------------------------------------
# --- Install required tools

RUN apt-get update -qq

# Base (non android specific) tools
# -> should be added to bitriseio/docker-bitrise-base

# Dependencies to execute Android builds
RUN apt-get install -y openjdk-8-jdk wget expect

# ------------------------------------------------------
# --- Download Android SDK tools into $ANDROID_HOME

RUN useradd -u 1000 -M -s /bin/bash android
RUN chown 1000 /opt

USER android
ENV ANDROID_SDK_HOME /opt/android-sdk-linux
ENV ANDROID_HOME /opt/android-sdk-linux

RUN cd /opt && wget -q https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -O android-sdk.tgz
RUN cd /opt && tar -xvzf android-sdk.tgz
RUN cd /opt && rm -f android-sdk.tgz

ENV PATH ${PATH}:${ANDROID_SDK_HOME}/tools:${ANDROID_SDK_HOME}/platform-tools:/opt/tools


# ------------------------------------------------------
# --- Install Android SDKs and other build packages

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
RUN echo y | android update sdk --no-ui --all --filter android-27 | grep 'package installed'

# build tools
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter build-tools-27.0.2 | grep 'package installed'


RUN echo y | android update sdk --no-ui --all --filter extra-android-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-google_play_services | grep 'package installed'

# Copy install tools
COPY tools /opt/tools

# Copy accepted android licenses
COPY licenses /opt/licenses

# Update SDK
RUN /opt/tools/android-accept-licenses.sh android update sdk --no-ui --obsolete --force

USER root

RUN apt-get clean

RUN mkdir -p ~/.gradle

RUN echo "org.gradle.jvmargs=-Xmx2048M -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8\n" >> ~/.gradle/gradle.properties
RUN echo "org.gradle.daemon=false\n" >> ~/.gradle/gradle.properties

VOLUME ["/opt/android-sdk-linux"]
