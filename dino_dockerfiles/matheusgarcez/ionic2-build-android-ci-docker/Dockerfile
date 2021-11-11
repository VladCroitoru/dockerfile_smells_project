FROM ubuntu:16.04
MAINTAINER Tobias Theobald <tobias@health-cast.com>

# Install apt packages
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get update && apt-get install -y git lib32stdc++6 lib32z1 s3cmd nodejs build-essential curl openjdk-8-jdk-headless sendemail libio-socket-ssl-perl libnet-ssleay-perl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install android SDK, tools and platforms
RUN cd /opt && curl https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -o android-sdk.tgz && tar xzf android-sdk.tgz && rm android-sdk.tgz
ENV ANDROID_HOME /opt/android-sdk-linux
RUN mkdir "%ANDROID_HOME%\licenses" && echo |set /p="8933bad161af4178b1185d1a37fbf41ea5269c55" > "%ANDROID_HOME%\licenses\android-sdk-license"
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | /opt/android-sdk-linux/tools/android update sdk --no-ui --filter platform-tools,build-tools-24.0.2,android-24,extra-android-support,extra-google-m2repository,extra-android-m2repository

# Install npm packages
RUN npm i -g cordova ionic gulp bower grunt phonegap typescript && npm cache clean

# Create dummy app to build and preload gradle and maven dependencies
RUN cd / && echo 'n' | ionic start app && cd /app && ionic platform add android && ionic build android && rm -rf * .??* && rm /root/.android/debug.keystore

WORKDIR /app
