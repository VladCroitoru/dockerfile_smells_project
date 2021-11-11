FROM ubuntu:16.04
MAINTAINER Hakan Dilek <hakandilek@gmail.com>

# Install node 7
RUN apt-get update && apt-get install -y apt-utils curl
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y nodejs

# Install other apt packages
RUN apt-get install -y git lib32stdc++6 lib32z1 s3cmd build-essential curl openjdk-8-jdk-headless sendemail libio-socket-ssl-perl libnet-ssleay-perl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install android SDK, tools and platforms 
RUN cd /opt && curl https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz -o android-sdk.tgz && tar xzf android-sdk.tgz && rm android-sdk.tgz
ENV ANDROID_HOME /opt/android-sdk-linux
RUN echo 'y' | /opt/android-sdk-linux/tools/android update sdk -u -a -t platform-tools,build-tools-23.0.3,android-23

# Install npm packages
RUN npm i -g cordova ionic gulp bower grunt node-gyp && npm cache clean

# Create dummy app to build and preload gradle and maven dependencies
RUN cd / && echo 'n' | ionic start app --v2 --ts && cd /app && ionic platform add android && ionic build android && rm -rf * .??* && rm /root/.android/debug.keystore

WORKDIR /app
