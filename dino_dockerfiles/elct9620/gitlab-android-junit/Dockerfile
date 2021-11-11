FROM java:8-jdk
MAINTAINER 蒼時弦也 docker@frost.tw

ENV ANDROID_SDK_VERSION r24.4.1
ENV ANDROID_SDK_SOURCE https://dl.google.com/android/android-sdk_${ANDROID_SDK_VERSION}-linux.tgz

RUN  apt-get update \
  && apt-get install -y ca-certificates lib32stdc++6 lib32z1 lib32z1-dev \
  && mkdir -p /opt

RUN curl -L ${ANDROID_SDK_SOURCE} | tar zxv -C /opt

ENV ANDROID_HOME /opt/android-sdk-linux

ENV PATH $PATH:$ANDROID_HOME/tools
ENV PATH $PATH:$ANDROID_HOME/platform-tools

RUN  echo "y" | android update sdk -u -a --filter tools \
  && echo "y" | android update sdk -u -a --filter platform-tools \
  && echo "y" | android update sdk -u -a --filter extra-android-support \
  && echo "y" | android update sdk -u -a --filter extra-android-m2repository \
  && echo "y" | android update sdk -u -a --filter extra-google-google_play_services \
  && echo "y" | android update sdk -u -a --filter extra-google-m2repository

RUN  echo "y" | android update sdk -u -a --filter android-23 \
  && echo "y" | android update sdk -u -a --filter build-tools-23.0.2 \
  && echo "y" | android update sdk -u -a --filter build-tools-23.0.1 \
  && echo "y" | android update sdk -u -a --filter build-tools-23.0.0

RUN  mkdir ~/.gradle \
	&& echo "org.gradle.daemon=true" >> ~/.gradle/gradle.properties \
	&& echo "org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8" >> ~/.gradle/gradle.properties \
	&& echo "org.gradle.parallel=true" >> ~/.gradle/gradle.properties \
	&& echo "org.gradle.configureondemand=true" >> ~/.gradle/gradle.properties \
