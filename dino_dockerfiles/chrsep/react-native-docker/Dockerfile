FROM debian:jessie

ENV ANDROID_COMPILE_SDK "23"
ENV ANDROID_BUILD_TOOLS "23.0.1"
ENV ANDROID_SDK_TOOLS "24.4.1"

ENV ANDROID_HOME=$PWD/android-sdk-linux
ENV PATH=$PATH:$PWD/android-sdk-linux/platform-tools/

RUN apt-get update && apt-get install -y curl

RUN echo 'deb http://http.debian.net/debian jessie-backports main' >> /etc/apt/sources.list
RUN curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh

RUN apt-get update
RUN apt-get install -t jessie-backports -y openjdk-8-jdk
RUN apt-get install -y nodejs \
                       wget \
                       tar \
                       unzip \
                       lib32stdc++6 \
                       lib32z1 \
    && apt-get clean

RUN npm install -g react-native-cli yarn && npm cache clean -g

RUN wget --quiet --output-document=android-sdk.tgz https://dl.google.com/android/android-sdk_r${ANDROID_SDK_TOOLS}-linux.tgz && \
    tar --extract --gzip --file=android-sdk.tgz && \
    rm android-sdk.tgz -fr

RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter android-${ANDROID_COMPILE_SDK} && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter android-25 && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter platform-tools && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter build-tools-${ANDROID_BUILD_TOOLS} && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter build-tools-25.0.2 && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter build-tools-23.0.3 && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-android-m2repository && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-google-google_play_services && \
          echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-google-m2repository
