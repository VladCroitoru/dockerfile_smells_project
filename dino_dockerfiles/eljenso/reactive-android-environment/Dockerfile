# Docker image for building react native Android releases

FROM node:6

MAINTAINER Jens Böttcher <eljenso.boettcher@gmail.com>

##
## Install Java
##
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && \
	apt-get install -qy --no-install-recommends sudo default-jdk

##
## Install Android SDK
##
# Set correct environment variables.
ENV ANDROID_SDK_FILE android-sdk_r24.4.1-linux.tgz
ENV ANDROID_SDK_URL http://dl.google.com/android/$ANDROID_SDK_FILE

# Install 32bit support for Android SDK
RUN dpkg --add-architecture i386 && \
    apt-get update -q && \
    apt-get install -qy --no-install-recommends libstdc++6:i386 libgcc1:i386 zlib1g:i386 libncurses5:i386

# Install Android SDK
ENV ANDROID_HOME /usr/local/android-sdk-linux
RUN cd /usr/local && \
    wget $ANDROID_SDK_URL && \
    tar -xzf $ANDROID_SDK_FILE && \
    chgrp -R users $ANDROID_HOME && \
    chmod -R 0775 $ANDROID_HOME && \
    rm $ANDROID_SDK_FILE

# Install android tools and system-image.
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/23.0.1
RUN echo "y" | android update sdk \
    --no-ui \
    --force \
    --all \
    --filter platform-tools,android-23,build-tools-23.0.1,build-tools-23.0.3,extra-android-support,extra-android-m2repository,extra-google-m2repository

# Clean up when done.
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    npm cache clear
