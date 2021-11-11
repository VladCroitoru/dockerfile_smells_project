FROM java:8-jdk
MAINTAINER Jerry <jerry@xqopen.com>
# refer to https://github.com/LiveXP/docker-android-sdk/blob/master/Dockerfile

# 国内源
# ADD sources.list /etc/apt/sources.list

ENV ANDROID_SDK_VERSION 24.4.1
ENV ANDROID_API_LEVELS android-21,android-22,android-23,android-24,android-25,android-26,android-27
ENV ANDROID_BUILD_TOOLS build-tools-25.0.3,build-tools-26.0.1,build-tools-27.0.3
ENV ANDROID_EXTRA addon-google_apis-google-23,extra-android-m2repository,extra-google-google_play_services,extra-google-m2repository,extra-google-market_apk_expansion,extra-google-market_licensing
ENV GRADLE_VERSION gradle-4.6


RUN update-ca-certificates -f

RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y openssh-client lib32z1 libc6:i386 libncurses5:i386 libstdc++6:i386

COPY bin/ /usr/local/bin/

RUN chmod 755 /usr/local/bin/docker-android-sdk-*

RUN wget -q https://dl.google.com/android/android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz && \
    tar zxvf android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz && \
    mv android-sdk-linux /usr/local/bin/android-sdk && \
    rm android-sdk_r${ANDROID_SDK_VERSION}-linux.tgz

ENV ANDROID_HOME /usr/local/bin/android-sdk
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

RUN docker-android-sdk-update && docker-android-sdk-install platform-tools,${ANDROID_API_LEVELS},${ANDROID_BUILD_TOOLS},${ANDROID_EXTRA}

RUN rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean

# install gradle
RUN wget -q  https://services.gradle.org/distributions/${GRADLE_VERSION}-bin.zip
RUN unzip ${GRADLE_VERSION}-bin.zip && mv /${GRADLE_VERSION} /usr/local/gradle
RUN export GRADLE_HOME=/usr/local/gradle && export PATH=$GRADLE_HOME/bin:$PATH
