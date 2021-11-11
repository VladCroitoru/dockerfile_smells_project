FROM frolvlad/alpine-oraclejdk8:slim
LABEL maintainer="Eric Chang <chiahan1123@gmail.com>"

# Android SDK environment variables
# Command line tools file from https://developer.android.com/studio/index.html
ENV ANDROID_SDK_HOME /usr/local/.android
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV ANDROID_TOOLS_FILE sdk-tools-linux-3859397.zip
ENV ANDROID_PACKAGES_FILE packagesFile.txt
ENV PATH $PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

# Gradle environment variables
ENV GRADLE_USER_HOME /usr/local/.gradle
ENV GRADLE_DEFAULT_VERSION 3.5
ENV GRADLE_DEFAULT_FILE gradle-${GRADLE_DEFAULT_VERSION}-bin.zip
ENV PATH $PATH:${GRADLE_USER_HOME}/gradle-${GRADLE_DEFAULT_VERSION}/bin

# bash -> gradle wrapper script
# git openssh -> checkout GitHub projects
# libstdc++ -> fixes the failed to load native library libnative-platform.so error
RUN apk update && apk upgrade && \
    apk add --no-cache wget bash git openssh libstdc++ && \
    rm -rf /var/cache/apk/*

# Installing Android SDK
WORKDIR $ANDROID_HOME
COPY $ANDROID_PACKAGES_FILE $ANDROID_PACKAGES_FILE
RUN wget https://dl.google.com/android/repository/${ANDROID_TOOLS_FILE} && \
    unzip $ANDROID_TOOLS_FILE && \
    rm $ANDROID_TOOLS_FILE && \
    echo y | sdkmanager --verbose --package_file=${ANDROID_PACKAGES_FILE} && \
    rm $ANDROID_PACKAGES_FILE

# Installing Default Gradle
WORKDIR $GRADLE_USER_HOME
RUN wget https://services.gradle.org/distributions/${GRADLE_DEFAULT_FILE} && \
    unzip $GRADLE_DEFAULT_FILE && \
    rm $GRADLE_DEFAULT_FILE
