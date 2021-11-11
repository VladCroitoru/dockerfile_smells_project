FROM jenkinsci/jnlp-slave
#FROM bitriseio/docker-bitrise-base-alpha:latest

#mayankkapoor: Need to set ANDROID_HOME as Android Jenkinsfile uses this directory. If you need to change this, change it in Android client Jenkinsfile also.
ENV ANDROID_HOME /var/lib/jenkins/tools/android-sdk

# ------------------------------------------------------
# --- Install required tools
USER root
# RUN apt-get update -y

# Base (non android specific) tools
# -> should be added to bitriseio/docker-bitrise-base

# Dependencies to execute Android builds
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386 || apt-get install -f && \
    rm -rf /var/lib/apt/lists/*


# ------------------------------------------------------
# --- Download Android SDK tools into $ANDROID_HOME
RUN cd /opt && wget -q https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip -O android-sdk-tools.zip && \
    unzip -q android-sdk-tools.zip && mkdir -p ${ANDROID_HOME} && mv tools/ ${ANDROID_HOME}/tools/ && \
    rm -f android-sdk-tools.zip

# ndk-bundle
# RUN cd /opt/android-sdk-linux/ && wget -q https://dl.google.com/android/repository/android-ndk-r15c-linux-x86_64.zip -O ndk-bundle.zip && \
#     unzip -q ndk-bundle.zip && mv android-ndk-r15c ndk-bundle && chown -R jenkins:jenkins ndk-bundle/

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

# ------------------------------------------------------
# --- Install Android SDKs and other build packages

# Other tools and resources of Android SDK
#  you should only install the packages you need!
# To get a full list of available options you can use:
#  sdkmanager --list
# (!!!) Only install one package at a time, as "echo y" will only work for one license!
#       If you don't do it this way you might get "Unknown response" in the logs,
#         but the android SDK tool **won't** fail, it'll just **NOT** install the package.
RUN echo y | ${ANDROID_HOME}/tools/bin/sdkmanager --update | grep done


# SDKs
# Please keep these in descending order!
# RUN echo y | android update sdk --no-ui --all --filter android-25 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-24 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-23 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-22 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter android-21 | grep 'package installed'

# build tools
# Please keep these in descending order!
# RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.3 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.2 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.1 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-25.0.0 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.3 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.2 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.1 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-24.0.0 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.3 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.2 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.1 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-22.0.1 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter build-tools-21.1.2 | grep 'package installed'


# Android System Images, for emulators
# Please keep these in descending order!
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-24 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter sys-img-armeabi-v7a-android-21 | grep 'package installed'

# Extras
# RUN echo y | android update sdk --no-ui --all --filter extra-android-m2repository | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter extra-google-m2repository | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter extra-google-google_play_services | grep 'package installed'

# google apis
# Please keep these in descending order!
# RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-23 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-22 | grep 'package installed'
# RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-21 | grep 'package installed'


# ------------------------------------------------------
# --- Install Gradle from PPA

# Gradle PPA
# RUN apt-get update && \
#     apt-get -y install gradle && \
#     gradle -v && \
#     rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------
# --- Install Maven 3 from PPA

# RUN apt-get -y purge maven && \
#     apt-get update && \
#     apt-get -y install maven && \
#     mvn --version && \
#     rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------
# --- Install Fastlane
# RUN gem install fastlane --no-document
# RUN fastlane --version

# copied from https://github.com/GoogleCloudPlatform/continuous-deployment-on-kubernetes
# ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
# ENV PATH /opt/google-cloud-sdk/bin:$PATH
# USER root
# RUN apt-get update -y && \
#     apt-get install -y jq && \
#     curl https://sdk.cloud.google.com | bash && mv google-cloud-sdk /opt && \
#     gcloud components install kubectl && \
#     rm -rf /var/lib/apt/lists/*

# added by Ackee
# RUN curl https://get.docker.com | bash

# fix HOME root env variables for android emulator plugin...
# WORKDIR /root
# ENV HOME /root
# RUN usermod -d /root jenkins && chown -R jenkins:root /root && \
#     chown -R jenkins:jenkins $ANDROID_HOME && chmod -R g+w $ANDROID_HOME

# ENV BITRISE_DOCKER_REV_NUMBER_ANDROID v2016_10_20_1
# CMD bitrise -version
# RUN echo y | ${ANDROID_HOME}/tools/bin/sdkmanager --update | grep done
