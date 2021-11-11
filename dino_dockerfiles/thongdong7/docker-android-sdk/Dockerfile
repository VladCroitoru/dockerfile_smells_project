FROM ubuntu:14.04

RUN apt-get --quiet update --yes \
  && apt-get --quiet install --yes wget tar unzip openjdk-7-jdk lib32stdc++6 lib32z1 curl build-essential \
  && wget --quiet --output-document=android-sdk.tgz https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz \
  && tar --extract --gzip --file=android-sdk.tgz \
  && echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter platform-tools,tools,build-tools-23.0.1,build-tools-23.0.3,android-23,extra-android-m2repository \
  && export ANDROID_HOME=$PWD/android-sdk-linux \
  && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
  && apt-get install -y nodejs
