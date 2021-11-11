FROM ubuntu:16.04

# Upgrade software
RUN apt-get update -y && apt-get upgrade -y

# Install Git
RUN apt-get install -y git
 
# Install sudo
RUN apt-get update \
  && apt-get -y install sudo \
  && useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
 
# Install 32bit lib
RUN sudo apt-get -y install lib32stdc++6 lib32z1

# Install unzip
RUN apt-get update \
  && sudo apt-get install unzip

# Install Java8
RUN apt-get install -y software-properties-common curl \
    && add-apt-repository -y ppa:openjdk-r/ppa \
    && apt-get update \
    && apt-get install -y openjdk-8-jdk
 
# Download Android SDK
ENV ANDROID_SDK_REVISION r24.4.1
RUN sudo apt-get -y install wget \
  && cd /usr/local \
  && wget http://dl.google.com/android/android-sdk_$ANDROID_SDK_REVISION-linux.tgz \
  && tar zxvf android-sdk_$ANDROID_SDK_REVISION-linux.tgz \
  && rm -rf /usr/local/android-sdk_$ANDROID_SDK_REVISION-linux.tgz
 
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV PATH $ANDROID_HOME/tools:$PATH

RUN echo y | android update sdk --no-ui --force --all --filter "tools"
RUN echo y | android update sdk --no-ui --force --all --filter "platform-tools"
RUN echo y | android update sdk --no-ui --force --all --filter "build-tools-23.0.3,build-tools-24.0.0,build-tools-24.0.1,build-tools-24.0.2,build-tools-24.0.3,build-tools-25,build-tools-25.0.1,build-tools-25.0.2,build-tools-25.0.3,build-tools-26,build-tools-26.0.1,build-tools-26.0.2"
RUN echo y | android update sdk --no-ui --force --all --filter "android-26,android-25,android-24,android-23,android-22,android-21"
RUN echo y | android update sdk --no-ui --force --all --filter "extra-android-m2repository,extra-google-m2repository"
 
# Licenses
Add android-sdk-license $ANDROID_HOME/licenses/
ENV TERM dumb
