FROM java:7-jdk
MAINTAINER cuervjos@gmail.com
RUN dpkg --add-architecture i386 \
 && apt-get -y update \
 && DEBIAN_FRONTEND=noninteractive apt-get -y install libncurses5:i386 libstdc++6:i386 zlib1g:i386 \
 && rm -rf /var/lib/apt/lists/*
# Downloading a copy of the android sdk
RUN wget --quiet --output-document=android-sdk.tgz https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz \
 && tar xvf android-sdk.tgz \
 && rm android-sdk.tgz \
 && mv /android-sdk-linux /sdk
RUN echo y | /sdk/tools/android update sdk -a -u --filter platform-tools,build-tools-22.0.1,android-23,android-22
RUN echo y | /sdk/tools/android update sdk -a -u --filter extra-google-google_play_services,extra-android-support
RUN echo y | /sdk/tools/android update sdk -a -u --filter extra-android-m2repository,extra-google-m2repository
RUN echo y | /sdk/tools/android update sdk -a -u --filter extra-google-google_play_services,extra-android-support,extra-android-m2repository
# Downloading a copy of gradle binaries
RUN wget --quiet --output-document=gradle.zip https://services.gradle.org/distributions/gradle-2.10-bin.zip \
 && unzip -q gradle.zip \
 && rm gradle.zip

ENV ANDROID_HOME=/sdk
ENV PATH=$PATH:/sdk/tools:/gradle-2.10/bin
