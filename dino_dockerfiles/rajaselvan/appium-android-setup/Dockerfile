FROM ubuntu:16.04

MAINTAINER Rajaselvan <rajaselvan@icloud.com>

RUN  echo "deb http://archive.ubuntu.com/ubuntu xenial main universe\n" > /etc/apt/sources.list \
  && echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main universe\n" >> /etc/apt/sources.list \
  && echo "deb http://security.ubuntu.com/ubuntu xenial-security main universe\n" >> /etc/apt/sources.list
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    ca-certificates \
    openjdk-8-jdk-headless \
    wget \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' ./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre
ENV PATH $PATH:$JAVA_HOME/bin
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
ENV ANDROID_SDK_URL="https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz" \
    ANDROID_BUILD_TOOLS_VERSION=25.0.0 \
    ANDROID_APIS="android-24,android-23,android-22,android-21,android-19" \
    ANDROID_HOME="/opt/android-sdk-linux"
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION
RUN dpkg --add-architecture i386 && \
          apt-get -qq update && \
          apt-get -qq install -y curl libncurses5:i386 libstdc++6:i386 zlib1g:i386  && \
    curl -sL ${ANDROID_SDK_URL} | tar xz -C /opt && \
    echo y | android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-tools-${ANDROID_BUILD_TOOLS_VERSION},sys-img-armeabi-v7a-android-24 && \
    chmod a+x -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove --purge -y && \
    apt-get clean
RUN adb start-server
RUN java -version
ENV NODEJS_VERSION=7.2.0 \
    PATH=$PATH:/opt/node/bin
WORKDIR "/opt/node"
RUN apt-get update -qqy \
    && apt-get install -y curl ca-certificates --no-install-recommends && \
    curl -sL https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz | tar xz --strip-components=1 && \
    npm install -g appium && \
    npm install appium-doctor -g && \
    npm cache clean && \
    apt-get remove --purge -y npm && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get clean
RUN node -v
RUN npm -v
RUN appium-doctor --android
ENV UDEV_REMOTE_FILE https://raw.githubusercontent.com/M0Rf30/android-udev-rules/master/51-android.rules
RUN mkdir /etc/udev/rules.d \
  && wget --no-verbose $UDEV_REMOTE_FILE -O /etc/udev/rules.d/51-android.rules
EXPOSE 4723

CMD ["appium"]
