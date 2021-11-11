FROM ruby:2.1.2

RUN apt-get update && apt-get -y install apt-utils \
		       build-essential \
		       git-core \
		       curl libssl-dev \
		       libreadline-dev \
		       zlib1g zlib1g-dev \
		       libmysqlclient-dev \
		       libcurl4-openssl-dev \
		       libxslt-dev libxml2-dev \
		       xvfb procps \
		       nodejs-legacy npm \
		       ruby-compass

ENV CONTAINER_INIT /usr/local/bin/init-container
RUN echo '#!/usr/bin/env bash' > $CONTAINER_INIT ; chmod +x $CONTAINER_INIT

RUN gem install bundler
RUN bundle config --global path /cache/bundle
RUN echo 'bundle config --global jobs $(cat /proc/cpuinfo | grep -c processor)' >> $CONTAINER_INIT

ENV LANG en_US.UTF-8
ENV GEM_HOME /cache

# Android SDK is i386 only
RUN dpkg --add-architecture i386 && \
      apt-get update -y && \
      apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 wget default-jdk && \
      rm -rf /var/lib/apt/lists/* && \
      apt-get autoremove -y && \
      apt-get clean

ENV JAVA_HOME /usr/lib/jvm/default-java

ENV ANDROID_SDK_VERSION 24.4.1
ENV ANDROID_API_LEVEL android-23
ENV ANDROID_BUILD_TOOLS_VERSION 23.0.1
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

RUN cd /opt && \
  wget -q http://dl.google.com/android/android-sdk_r$ANDROID_SDK_VERSION-linux.tgz && \
  tar -xzf android-sdk_r$ANDROID_SDK_VERSION-linux.tgz && \
  rm android-sdk_r$ANDROID_SDK_VERSION-linux.tgz && \
echo y | android update sdk --no-ui -a --filter extra,tools,platform-tools,${ANDROID_API_LEVEL},build-tools-${ANDROID_BUILD_TOOLS_VERSION}

RUN apt-get update && apt-get -y install ant
