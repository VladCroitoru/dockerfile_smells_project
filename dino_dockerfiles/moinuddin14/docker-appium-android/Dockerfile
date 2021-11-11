FROM ubuntu:16.04

MAINTAINER Khaja M Mohammed <moinuddinbtech14@gmail.com>

#===============================
# Customize sources for apt-get
#===============================


#===================================
# Set Up Java
# --no-install-recommends is used to 
# save space on the container disk
# Adding Make as getting error wget not found. 
#===================================

# RUN apt-get update -qqy && apt-get -qqy --no-install-recommends install openjdk-8-jdk-headless && apt-get install -qqy wget

# RUN ["make", "-C", "/usr/local/zlib", "install"]

RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    ca-certificates \
    openjdk-8-jdk-headless \
    wget
#    sudo \
#    unzip
#    tar=1.22-2ubuntu1
#    tar
#    tar.x86_64
# && rm -rf /var/lib/apt/lists/* \
# && sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' ./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security


#============================================================
# Set Up Android SDK
# Android Studio Link: 
# https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
# https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
# Using Direct Path to WGet as getting error unable to find WGet
#============================================================
ENV ANDROID_SDK_VERSION 24.4.1
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH {PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:/usr/bin/wget:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
ENV ANDROID_TOOLS platform-tools,build-tools-24.0.0
# RUN chmod -R 777 /usr/lib/tar
RUN cd /opt
# RUN wget "http://dl.google.com/android/android-sdk_r$ANDROID_SDK_VERSION-linux.tgz" -O android-sdk.tgz \
# && tar -xf  android-sdk.tgz \
RUN wget -qO- https://dl.google.com/android/android-sdk_r$ANDROID_SDK_VERSION-linux.tgz | tar -zxv -C /opt/
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --all --filter platform-tools,build-tools-20.0.0 --no-ui --force \
&& rm -rf android-sdk.tgz \
# && echo y | android update sdk --all --force --no-ui --filter ${ANDROID_TOOLS}

#===================================
# Set Up NodeJS and APPIUM
#===================================

ENV APPIUM_VERSION 1.5.3
RUN apt-get update -qqy
RUN apt-get install -qqy nodejs \
&& apt-get install -qqy npm \
&& ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g appium@$APPIUM_VERSION \
&& npm cache clean \
# && apt-get remove --purge -y npm \
# && apt-get autoremove --purge -y \
# && rm -rf /var/lib/apt/lists/*

#===============================================================
# Add udev rules file with USB configuration
# Check this URL for more details of why it is needed
# https://developer.android.com/studio/run/device.html#VendorIds
#===============================================================

ENV UDEV_FILE https://github.com/moinuddin14/Ubuntu-Linux-USB-Vendor-IDs/blob/master/51-android.rules
RUN mkdir /etc/udev/rules.d \
&& wget --no-verbose https://github.com/moinuddin14/Ubuntu-Linux-USB-Vendor-IDs/blob/master/51-android.rules -O /etc/udev/rules.d/51-android.rules \
&& chmod a+r /etc/udev/rules.d/51-android.rules

#============================================
# Expose APPIUM Server Port
#============================================

EXPOSE 4723

#==================
# Run APPIUM Server
#==================

CMD appium
