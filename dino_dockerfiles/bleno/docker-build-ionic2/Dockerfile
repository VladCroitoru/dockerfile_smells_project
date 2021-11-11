FROM ubuntu:14.04

MAINTAINER Bleno <blenobok@gmail.com>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y wget curl tar  build-essential software-properties-common \
    && add-apt-repository ppa:webupd8team/java -y

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g cordova \
    && npm install -g ionic

# https://developer.android.com/studio/install.html?pkg=tools
# lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6
# python for general scripts
# sendemail for send email notification
# java8 oracle
RUN  apt-get update \
     && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
     && apt-get install -y python git make zip oracle-java8-installer \
     libnet-ssleay-perl libio-socket-ssl-perl sendemail \
     lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6


# https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip?hl=pt-br
RUN mkdir -p /opt/android-sdk \
    && cd /opt/android-sdk \
    && wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip \
    # && wget   https://dl.google.com/android/repository/tools_r25.2.5-linux.zip \
    && unzip sdk-tools-linux-3859397.zip \
    && mkdir ~/.android \
    && touch ~/.android/repositories.cfg
    # && unzip tools_r25.2.5-linux.zip


RUN echo y | /opt/android-sdk/tools/bin/sdkmanager --sdk_root=/opt/android-sdk/ "build-tools;27.0.3" "sources;android-27" "extras;android;m2repository" "extras;google;m2repository" "extras;google;google_play_services"


RUN mkdir -p /opt/gradle \
    && cd /opt/gradle \
    && wget https://services.gradle.org/distributions/gradle-4.6-bin.zip \
    && unzip gradle-4.6-bin.zip

ENV ANDROID_SDK_ROOT=/opt/android-sdk 

# # develop environment
ENV ANDROID_HOME=/opt/android-sdk \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle/ \
    GRADLE=/opt/gradle/gradle-4.6/bin \

# Add environment variable ANDROID_SDK_ROOT
    PATH=$ANDROID_SDK_ROOT:$PATH \
    PATH=$ANDROID_SDK_ROOT/tools:$ANDROID_SDK_ROOT/platform-tools:$PATH

ENV PATH=$GRADLE:$PATH

RUN rm /opt/android-sdk/sdk-tools-linux-3859397.zip \
    && apt-get -y autoclean && apt-get -y autoremove \
    && rm -rf /tmp/* \
    && rm -rf /opt/android-sdk/temp/* \
    && rm -f /opt/gradle/gradle-4.6-bin.zip

RUN mkdir /project

#entrypoint
WORKDIR /project

