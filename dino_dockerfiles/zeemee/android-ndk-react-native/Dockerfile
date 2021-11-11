FROM bitriseio/docker-bitrise-base:latest

ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_NDK_HOME /opt/android-ndk


# ------------------------------------------------------
# --- Install required tools

RUN apt-get update -qq
# Dependencies to execute Android builds
RUN dpkg --add-architecture i386
RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk libc6:i386 libstdc++6:i386 libgcc1:i386 libncurses5:i386 libz1:i386

# ------------------------------------------------------
# --- Download Android SDK tools into $ANDROID_HOME

RUN cd /opt && wget -q https://dl.google.com/android/repository/tools_r25.2.4-linux.zip -O android-sdk-tools.zip
RUN cd /opt && unzip -q android-sdk-tools.zip
RUN mkdir -p ${ANDROID_HOME}
RUN cd /opt && mv tools/ ${ANDROID_HOME}/tools/
RUN cd /opt && rm -f android-sdk-tools.zip

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

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

# SDKs
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter android-23 | grep 'package installed'

# build tools
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter build-tools-23.0.1 | grep 'package installed'

# Extras
RUN echo y | android update sdk --no-ui --all --filter extra-android-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-m2repository | grep 'package installed'
RUN echo y | android update sdk --no-ui --all --filter extra-google-google_play_services | grep 'package installed'

# google apis
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter addon-google_apis-google-23 | grep 'package installed'


# ------------------------------------------------------
# --- Install Gradle from PPA

# Gradle PPA
RUN apt-get update
RUN apt-get -y install gradle
RUN gradle -v

# ------------------------------------------------------
# --- Install Maven 3 from PPA

RUN apt-get purge maven maven2
RUN apt-get update
RUN apt-get -y install maven
RUN mvn --version

# ------------------------------------------------------
# --- Install Fastlane

RUN gem install fastlane --no-document
RUN fastlane --version

# ------------------------------------------------------
# --- Install Google Cloud SDK
# https://cloud.google.com/sdk/downloads
#  Section: apt-get (Debian and Ubuntu only)
#
# E.g. for "Using Firebase Test Lab for Android from the gcloud Command Line":
#  https://firebase.google.com/docs/test-lab/command-line
#

RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-`lsb_release -c -s` main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
RUN sudo apt-get update -qq
RUN sudo apt-get install -y -qq google-cloud-sdk

ENV GCLOUD_SDK_CONFIG /usr/lib/google-cloud-sdk/lib/googlecloudsdk/core/config.json

# gcloud config doesn't update config.json. See the official Dockerfile for details:
#  https://github.com/GoogleCloudPlatform/cloud-sdk-docker/blob/master/Dockerfile
RUN /usr/bin/gcloud config set --installation component_manager/disable_update_check true
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g' $GCLOUD_SDK_CONFIG

RUN /usr/bin/gcloud config set --installation core/disable_usage_reporting true
RUN sed -i -- 's/\"disable_usage_reporting\": false/\"disable_usage_reporting\": true/g' $GCLOUD_SDK_CONFIG


# ------------------------------------------------------
# --- Install additional packages

# Required for Android ARM Emulator
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libqt5widgets5

# ------------------------------------------------------
# --- Android NDK

# download
RUN mkdir /opt/android-ndk-tmp
RUN cd /opt/android-ndk-tmp && wget -q http://dl.google.com/android/repository/android-ndk-r10e-linux-x86_64.zip
# uncompress
RUN cd /opt/android-ndk-tmp && unzip -q android-ndk-r10e-linux-x86_64.zip
# move to its final location
RUN cd /opt/android-ndk-tmp && mv ./android-ndk-r10e ${ANDROID_NDK_HOME}
# remove temp dir
RUN rm -rf /opt/android-ndk-tmp
# add to PATH
ENV PATH ${PATH}:${ANDROID_NDK_HOME}


# ------------------------------------------------------
# --- Android CMake

# download
RUN mkdir /opt/android-cmake-tmp
RUN cd /opt/android-cmake-tmp && wget -q https://dl.google.com/android/repository/cmake-3.6.3155560-linux-x86_64.zip -O android-cmake.zip
# uncompress
RUN cd /opt/android-cmake-tmp && unzip -q android-cmake.zip -d android-cmake
# move to its final location
RUN cd /opt/android-cmake-tmp && mv ./android-cmake ${ANDROID_HOME}/cmake
# remove temp dir
RUN rm -rf /opt/android-cmake-tmp
# add to PATH
ENV PATH ${PATH}:${ANDROID_HOME}/cmake/bin


# ------------------------------------------------------
# --- Cleanup and rev num

# Cleaning
RUN apt-get clean

CMD bitrise -version
