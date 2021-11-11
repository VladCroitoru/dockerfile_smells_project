FROM openjdk:8

MAINTAINER Tamas Mohos <tomi@mohos.name>

# Set up args
ARG ANDROID_SYSTEM_PACKAGE_VERSION="28"
ARG ANDROID_BUILD_TOOLS_PACKAGE_VERSION="28.0.2"
ARG NODE_VERSION="11.2.0"
ARG GRADLE_VERSION="4.10.2"
ARG ANDROID_SDK_ZIP_VERSION="4333796"

# Set up environment variables
ENV ANDROID_HOME="/root/android-sdk-linux" \
    SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_ZIP_VERSION}.zip" \
    GRADLE_URL="https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"

# Install Git and dependencies
RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y file git curl zip libncurses5:i386 libstdc++6:i386 zlib1g:i386 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists /var/cache/apt

# Installs Node.js
RUN wget http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz \
    && tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz \
    && mv node-v${NODE_VERSION}-linux-x64 /opt/node \
    && rm node-v${NODE_VERSION}-linux-x64.tar.gz

ENV PATH ${PATH}:/opt/node/bin

# Installs nativescript
RUN npm config set unsafe-perm true \
    && npm install -g nativescript \
    && tns usage-reporting disable \
    && tns error-reporting disable

# Download Android SDK
RUN mkdir "${ANDROID_HOME}" .android \
    && cd "${ANDROID_HOME}" \
    && curl -o sdk.zip ${SDK_URL} \
    && unzip sdk.zip \
    && rm sdk.zip \
    && yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses

# Install Gradle
RUN wget ${GRADLE_URL} -O gradle.zip \
    && unzip gradle.zip \
    && mv gradle-${GRADLE_VERSION} .gradle/ \
    && rm gradle.zip \
    && cd .gradle \
    && bin/gradle wrapper --distribution-type all \
    && ./gradlew build

# Set path env
ENV PATH="/home/user/.gradle/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${PATH}"

# Download android sdk tools
RUN ${ANDROID_HOME}/tools/bin/sdkmanager \
    "tools" "platform-tools" "platforms;android-${ANDROID_SYSTEM_PACKAGE_VERSION}" \
    "build-tools;${ANDROID_BUILD_TOOLS_PACKAGE_VERSION}" "extras;android;m2repository" "extras;google;m2repository"

RUN mkdir /root/project
WORKDIR /root/project
