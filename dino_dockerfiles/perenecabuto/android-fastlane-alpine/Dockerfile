FROM openjdk:alpine

LABEL maintainer "Felipe Ramos (Cabuto) <perenecabuto@gmail.com>"


ENV ANDROID_SDK_TOOLS_VERSION="3859397"
ENV ANDROID_HOME="/usr/local/android-sdk"
ENV ANDROID_VERSION=27
ENV ANDROID_BUILD_TOOLS_VERSION=27.0.2
ENV FASTLANE_VERSION=2.80.0
ENV GLIBC_VERSION=2.29-r0

ENV SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip"
ENV DOWNLOAD_FILE=/tmp/sdk.zip

# Deps
RUN apk add --update \
    ca-certificates \
    wget \
    unzip \
    libstdc++ \
    g++ \
    make \
    ruby \
    ruby-irb \
    ruby-dev \
    && rm -rf /var/cache/apk/*

# Fastlane
RUN gem install fastlane -N -v $FASTLANE_VERSION

# Android SDK
RUN mkdir -p "$ANDROID_HOME" \
    && wget -q -O "$DOWNLOAD_FILE" $SDK_URL \
    && unzip "$DOWNLOAD_FILE" -d "$ANDROID_HOME" \
    && rm "$DOWNLOAD_FILE" \
    && yes | $ANDROID_HOME/tools/bin/sdkmanager --update \
    && yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses


# Android Build Tools
RUN $ANDROID_HOME/tools/bin/sdkmanager --update
RUN $ANDROID_HOME/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
    "platforms;android-${ANDROID_VERSION}" \
    "platform-tools"

# AIDL deps
RUN apk --no-cache add ca-certificates wget
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub

RUN mkdir -p /tmp/glibc
RUN for PACKAGE in glibc glibc-bin glibc-i18n glibc-dev; do \
        export APK_FILE="${PACKAGE}-${GLIBC_VERSION}.apk"; \
        export APK_PATH="/tmp/glibc/$APK_FILE"; \
        wget -q -O $APK_PATH https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/${APK_FILE}; \
        apk add $APK_PATH; \
    done

RUN rm -rf /tmp/glibc
