FROM ubuntu:16.04

MAINTAINER Elliot Tormey <elliot@tapadoo.com>

ENV DOCKER true
ENV ANDROID_HOME /opt/android

# ------------------------------------------------------
# --- Install required tools
# ------------------------------------------------------

RUN apt-get update
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gradle unzip git curl wget openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386

# ------------------------------------------------------
# --- Download Android SDK tools into $ANDROID_HOME
# ------------------------------------------------------

RUN mkdir $ANDROID_HOME
RUN cd $ANDROID_HOME && wget -q https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip -O android-sdk.zip
RUN cd $ANDROID_HOME && unzip android-sdk.zip && rm -f android-sdk.zip
ENV PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin

# ------------------------------------------------------
# --- Install Android SDKs and other build packages
# ------------------------------------------------------

# Other tools and resources of Android SDK you should only install the packages you need!
# To get a full list of available options you can use:
#     sdkmanager --list

RUN echo y | sdkmanager "platform-tools"

# Build tools
RUN echo y | sdkmanager "build-tools;26.0.0"
RUN echo y | sdkmanager "build-tools;25.0.3"

# SDKs
RUN echo y | sdkmanager "platforms;android-26"
RUN echo y | sdkmanager "platforms;android-25"
RUN echo y | sdkmanager "platforms;android-24"

# Extras
RUN echo y | sdkmanager "extras;android;m2repository"
RUN echo y | sdkmanager "extras;google;m2repository"
RUN echo y | sdkmanager "extras;google;google_play_services"

# Final update just to be sure to be sure
RUN echo y | sdkmanager --update

# ------------------------------------------------------
# --- Cleanup and rev num
# ------------------------------------------------------

# Cleaning
RUN apt-get clean
