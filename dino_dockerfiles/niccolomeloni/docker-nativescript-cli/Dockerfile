FROM ubuntu:latest

LABEL maintainer "niccolomeloni@gmail.com"

ARG ANDROID_SDK_URL="https://dl.google.com/android/repository/tools_r25.2.3-linux.zip"
ARG ANDROID_BUILD_TOOLS="build-tools-25.0.2"
ARG ANDROID_APIS="android-21,android-22,android-23,android-24,android-25"
ARG ANDROID_EXTRA_PACKAGES="extra-android-m2repository,extra-google-m2repository,extra-google-google_play_services"

RUN useradd -m tns

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends 	apt-transport-https \
						build-essential \
						curl \
						g++ \
						git \
						gradle \
						lib32z1 \
						libc6 \
						lib32ncurses5 \
						lib32stdc++6 \
						maven \
						openjdk-8-jdk \
						software-properties-common \
						unzip \
						usbutils

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
    apt-get update && \
    apt-get install -y --no-install-recommends 	nodejs						

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /tns /opt/android-sdk

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV ANDROID_HOME /opt/android-sdk

RUN curl -o android-sdk.zip ${ANDROID_SDK_URL} && \
    unzip -q android-sdk.zip -d ${ANDROID_HOME} && \
    rm -f android-sdk.zip

RUN echo y | ${ANDROID_HOME}/tools/android update sdk --all --no-ui --filter platform-tools,${ANDROID_BUILD_TOOLS},${ANDROID_APIS},${ANDROID_EXTRA_PACKAGES}

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

RUN npm install nativescript -g --unsafe-perm && \
    tns error-reporting disable && \
    tns usage-reporting disable

RUN chown tns:tns -R ${ANDROID_HOME} /tns

USER tns

WORKDIR /tns
