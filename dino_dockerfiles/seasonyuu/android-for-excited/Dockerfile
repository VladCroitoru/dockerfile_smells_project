# forked from https://github.com/snowdream/dockerfiles/blob/master/android/sdk/Dockerfile
FROM snowdream/gradle:latest

# MAINTAINER snowdream <yanghui1986527@gmail.com>
MAINTAINER seasonyuu <seasonyuu@gmail.com>

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qqy install libc6:i386 libstdc++6:i386 zlib1g:i386 libncurses5:i386 tar git zip --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*


# Download and unzip Gradle
RUN cd /usr/local/ && curl -L -O http://services.gradle.org/distributions/gradle-2.14.1-all.zip && unzip -o gradle-2.14.1-all.zip

# Download and untar Android SDK
ENV ANDROID_SDK_URL https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
RUN curl -sSL "${ANDROID_SDK_URL}" | tar --no-same-owner -xz -C ${SDK_HOME}
ENV ANDROID_HOME ${SDK_HOME}/android-sdk-linux
ENV GRADLE_HOME /usr/local/gradle-2.14.1
ENV ANDROID_SDK ${SDK_HOME}/android-sdk-linux
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$GRADLE_HOME/bin:$PATH

# Install Android SDK components

ENV ANDROID_COMPONENTS platform-tools,build-tools-25.0.0,build-tools-25.0.2,android-25
ENV GOOGLE_COMPONENTS extra-android-m2repository,extra-google-m2repository

RUN rm -rf /usr/local/gradle-2.14.1-all.zip
RUN echo y | android update sdk --no-ui --all --filter "${ANDROID_COMPONENTS}" ; \
    echo y | android update sdk --no-ui --all --filter "${GOOGLE_COMPONENTS}"
