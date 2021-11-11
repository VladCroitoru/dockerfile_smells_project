FROM ubuntu:16.04

# Install ENV
ENV ANDROID_HOME=/opt/android-sdk-linux \
    NODE_VERSION=8.4.0 \
    NPM_VERSION=5.3.0 \
    IONIC_VERSION=3.9.0 \
    CORDOVA_VERSION=7.0.1 \
    # Fix for the issue with Selenium, as described here:
    # https://github.com/SeleniumHQ/docker-selenium/issues/87
    DBUS_SESSION_BUS_ADDRESS=/dev/null

# PPA Setup
RUN apt-get update
RUN apt-get purge maven maven2
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:cwchien/gradle
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:openjdk-r/ppa
#RUN add-apt-repository ppa:andrei-pozolotin/maven3
RUN apt-get update

# Install Basics
RUN apt-get install -y --fix-missing git wget curl unzip ruby build-essential xvfb ifupdown libxtables11 javascript-common libglapi-mesa xfonts-utils openjdk-7-jre  openjdk-7-jdk libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable ttf-ubuntu-font-family libfreetype6 libfontconfig

# Download Android SDK tools into $ANDROID_HOME

RUN cd /opt && wget -q https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -O android-sdk.tgz
RUN cd /opt && tar -xvzf android-sdk.tgz
RUN cd /opt && rm -f android-sdk.tgz

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

# Install Android SDKs and other build packages

# To get a full list of available options you can use:
#  android list sdk --no-ui --all --extended
RUN echo y | android update sdk --no-ui --all --filter \
  platform-tools,extra-android-support

# google apis
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter \
  addon-google_apis-google-23,addon-google_apis-google-22,addon-google_apis-google-21

# SDKs
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter \
  android-N,android-23,android-22,android-21,android-20,android-19,android-17,android-15,android-10
# build tools
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter \
  build-tools-24.0.0-preview,build-tools-23.0.2,build-tools-23.0.1,build-tools-22.0.1,build-tools-21.1.2,build-tools-20.0.0,build-tools-19.1.0,build-tools-17.0.0

# Android System Images, for emulators
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter \
  sys-img-armeabi-v7a-android-23,sys-img-armeabi-v7a-android-22,sys-img-armeabi-v7a-android-21,sys-img-armeabi-v7a-android-19,sys-img-armeabi-v7a-android-17,sys-img-armeabi-v7a-android-16,sys-img-armeabi-v7a-android-15

# Extras
RUN echo y | android update sdk --no-ui --all --filter \
  extra-android-m2repository,extra-google-m2repository,extra-google-google_play_services

# Install Gradle from PPA

RUN apt-get -y install gradle
RUN gradle -v

# Install Maven 3
#RUN apt-get -y --fix-missing install maven3

# Get maven 3.3.9
RUN wget --no-verbose -O /tmp/apache-maven-3.3.9-bin.tar.gz http://www-eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz

# Install maven
RUN tar xzf /tmp/apache-maven-3.3.9-bin.tar.gz -C /opt/
RUN ln -s /opt/apache-maven-3.3.9 /opt/maven
RUN ln -s /opt/maven/bin/mvn /usr/local/bin
RUN rm -f /tmp/apache-maven-3.3.9-bin.tar.gz
ENV MAVEN_HOME /opt/maven
RUN mvn --version


# Cleaning
RUN apt-get clean


# Install Node, Cordova & Ionic
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" && \
    tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 && \
    rm "node-v$NODE_VERSION-linux-x64.tar.gz" && \
    npm install -g npm@"$NPM_VERSION" cordova@"$CORDOVA_VERSION" ionic@"$IONIC_VERSION" && \
    mkdir app

# when we change our application's nodejs dependencies:
#ADD package.json /tmp/package.json
RUN apt-get install -y python python-pip
#RUN cd /tmp && npm install

WORKDIR app
EXPOSE 8100 35729

CMD ["ionic", "serve"]
 
