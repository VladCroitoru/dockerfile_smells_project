# based on https://hub.docker.com/r/gfx2015/android/ with openjdk-8
FROM openjdk:8

MAINTAINER Nam Nguyen <nam@ene.im>

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y git && \
    apt-get install -yq libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386 --no-install-recommends && \
    apt-get clean

# Download and untar SDK
ENV ANDROID_SDK_URL http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
# ENV ANDROID_SDK_URL http://dl.google.com/android/android-sdk_r25.1.7-linux.tgz
RUN curl -L "${ANDROID_SDK_URL}" | tar --no-same-owner -xz -C /usr/local
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV ANDROID_SDK /usr/local/android-sdk-linux
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH

# SDK licenses agreements
RUN mkdir "$ANDROID_SDK/licenses" || true
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "$ANDROID_SDK/licenses/android-sdk-license"
RUN echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_SDK/licenses/android-sdk-preview-license"

# Install Android SDK components

# License Id: android-sdk-license-ed0d0a5b
ENV ANDROID_COMPONENTS platform-tools,build-tools-25.0.2,build-tools-26.0.1,android-25,android-26
# License Id: android-sdk-license-5be876d5
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-google-m2repository

RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}" ; \
    echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"

# Support Gradle
ENV TERM dumb
